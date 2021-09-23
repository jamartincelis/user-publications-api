"""
Archivos auxiliar para agregar sentencias sql planas.
"""

BALANCE_MENSUAL = """
select month_name, coalesce(incomes,0) as incomes, coalesce(expenses,0) as expenses, coalesce(incomes,0)-coalesce(abs(expenses),0) as balance, %s as year from (
	SELECT *
	FROM crosstab(
	       'select * from (
				SELECT   trim(max(TO_CHAR(transaction_date, ''Month''))) AS month_name,
						 EXTRACT(MONTH from transaction_date) as month_number,
	                     sum(amount) as total
				FROM transactions  
				WHERE amount > 0
				AND user_id = '%s'
                and EXTRACT(YEAR from transaction_date) = '%s'
				group by EXTRACT(MONTH from transaction_date)
				union all
				SELECT   trim(max(TO_CHAR(transaction_date, ''Month''))) AS month_name,
						 EXTRACT(MONTH from transaction_date) as month_number,
	                     sum(amount) as total			
	            FROM transactions  
				WHERE amount < 0
				AND user_id = '%s'
                and EXTRACT(YEAR from transaction_date) = '%s'
				group by EXTRACT(MONTH from transaction_date)
			) balance_total 
			order by balance_total.month_number, balance_total.total desc'
	 ) 
	 AS ct (month_name text, incomes numeric, expenses numeric)
) balance
"""

EGRESOS_PRESUPUESTOS = """
select * from (
	select balance.*,
	       round(((abs(spend)*100)/total_expenses.amount),2) as "percentage"
	from ( 
		select  max(c.description) as category,
				abs(SUM(t.amount)) AS spend, 
				COUNT(1) AS movements
		FROM transactions t
		inner join codes c
			on t.category_id = c.id
		WHERE t.amount < 0
		AND t.transaction_date BETWEEN %s AND %s 
		AND t.user_id = %s
		GROUP BY t.category_id ORDER BY t.category_id ASC
	) balance,
	(
		select sum(abs(amount)) as amount
		FROM transactions 
		WHERE user_id = %s
		and amount < 0 
		AND transaction_date BETWEEN %s AND %s
	) total_expenses
) egresos_presupuestos
order by egresos_presupuestos.percentage desc
"""

ANIOS_TRANSACCIONES = """
select * from (
	select distinct (EXTRACT(YEAR from transaction_date))::numeric::integer as y
	from transactions t where user_id = '479ec168-0139-45d0-b704-2bc4e5d0c4fb'
) years
order by years.y desc
"""