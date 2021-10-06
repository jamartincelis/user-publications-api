from django.contrib import admin

from budget.models import Budget


class BudgetAdminAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'category',
        'amount',
        'budget_date'
    ]

admin.site.register(Budget, BudgetAdminAdmin)
