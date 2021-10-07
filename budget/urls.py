from django.urls import path

from budget.views import BudgetList, BudgetDetail, Category


urlpatterns = [
    path('', BudgetList.as_view()),
    path('<str:pk>/', BudgetDetail.as_view()),
    path('categories/<str:category>/', Category.as_view()),
]
