from django.urls import path
from . import views

app_name = "budget"
urlpatterns = [
    path('', views.BudgetList.as_view(), name='budgets'),
    path('<int:pk>/', views.BudgetDetail.as_view()),
]