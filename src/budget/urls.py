from django.urls import path

from budget.views import BudgetsList, BudgetDetail, BudgetByMonthAndCategory


urlpatterns = [
    path('', BudgetsList.as_view()),
    path('<str:pk>/', BudgetDetail.as_view()),
    path('categories/<str:category_id>/', BudgetByMonthAndCategory.as_view())
]
