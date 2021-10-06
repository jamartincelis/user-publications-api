from django.urls import path, include

from transaction import views


urlpatterns = [
    path('', views.TransactionList.as_view()),
    path('expenses/summary/', views.ExpenseSummaryView.as_view()),
    path('summary/', views.CategorySummary.as_view()),
    path('balance/', views.MonthlyBalanceView.as_view()),
    path('<str:pk>/', views.TransactionDetail.as_view()),
    path('categories/<str:category>/', views.Category.as_view()),
    path('balance/category/<str:category>/', views.MonthlyCategoryBalanceView.as_view()),
]
