from django.urls import path, include

from transaction.views import TransactionsByMonth, TransactionDetail, TransactionsByCategoryAndMonth,\
    TransactionsCategoriesSummarybyMonth, ExpensesSummary, MonthlyBalance, MonthlyCategoriesBalance


urlpatterns = [
    path('', TransactionsByMonth.as_view()),
    path('expenses/summary/', ExpensesSummary.as_view()),
    path('summary/', TransactionsCategoriesSummarybyMonth.as_view()),
    path('balance/', MonthlyBalance.as_view()),
    path('categories/<str:category>/', TransactionsByCategoryAndMonth.as_view()),
    path('balance/category/<str:category>/', MonthlyCategoriesBalance.as_view()),
    path('<str:pk>/', TransactionDetail.as_view())
]
