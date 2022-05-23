from django.urls import path

from budget.views import BudgetsList, BudgetDetail, BudgetsByMonthAndCategory


urlpatterns = [
    path('', BudgetsList.as_view()),
    path('<str:pk>/', BudgetDetail.as_view()),
    path('categories/<str:category_id>/', BudgetsByMonthAndCategory.as_view())
]
