import pendulum
from django_extensions.management.jobs import MonthlyJob
from budget.models import Budget

class Job(MonthlyJob):
    help = "Duplicar presupuestos Job."
    def execute(self):
        """
        Se ejecuta mensualmente y obtiene el presupuesto del mes anterior del usuario 
        y lo duplica al mes actual.  
        """
        now = pendulum.now()
        month = pendulum.now().month
        last_month = month-1
        last_month_budgets = Budget.objects.filter(budget_date__month=last_month)
        budgets_bulk_list = []
        for last_budget in last_month_budgets:
            try:
                Budget.objects.get(
                    user_id=last_budget.user_id,
                    category_id=last_budget.category_id,
                    budget_date__month=month)
            except Budget.DoesNotExist:
                budgets_bulk_list.append({
                    'user': last_budget.user,
                    'category': last_budget.category,
                    'budget_date': now
                })
        Budget.objects.bulk_create([Budget(**budget) for budget in budgets_bulk_list])