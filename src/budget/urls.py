from django.urls import path

from budget.views import BudgetsList, BudgetDetail, BudgetsByMonthAndCategory


urlpatterns = [
    # retorna los presupuestos del usuario
    path('', BudgetsList.as_view()),
    # retorna el detalle de un presupuesto y permite la actualziación de su estado
    path('<str:pk>/', BudgetDetail.as_view()),
    # retorna los presupuestos por mes y categoría
    path('categories/<str:category_id>/', BudgetsByMonthAndCategory.as_view())
]
