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