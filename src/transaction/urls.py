from django.urls import path
from transaction import views

app_name = "transaction"

urlpatterns = [
    path('', views.TransactionList.as_view(), name="list"),
    path('expenses/summary/', views.ExpenseSummaryView.as_view(), name="expenses_summary"),
    path('summary/', views.CategorySummary.as_view(), name="summary"),
    path('balance/', views.MonthlyBalanceView.as_view(), name="balance"),
    path('<str:pk>/', views.TransactionDetail.as_view(), name="detail"),
    path('categories/<str:category>/', views.Category.as_view()),
    path('balance/category/<str:category>/', views.MonthlyCategoryBalanceView.as_view()),
]
