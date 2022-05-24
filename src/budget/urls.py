from django.urls import path

from budget.views import BudgetList, BudgetDetail, Category

app_name = "budget"

urlpatterns = [
    path('', BudgetList.as_view(), name="list"),
    path('<str:pk>/', BudgetDetail.as_view(), name="detail"),
    path('categories/<str:category>/', Category.as_view())
]
