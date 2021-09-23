from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "transaction"

urlpatterns = [
    path('expenses/summary/', views.ExpenseSummaryView.as_view()),
    path('summary/', views.CategorySummary.as_view()),
    path('balance/', views.MonthlyBalanceView.as_view()),
    path('', views.TransactionList.as_view()),
    path('<str:pk>/', views.TransactionDetail.as_view()),
    path('categories/<str:category>/', views.Category.as_view()),
]
