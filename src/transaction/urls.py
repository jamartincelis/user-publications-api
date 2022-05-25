from django.urls import path, include

from transaction.views import TransactionsByMonth, TransactionDetail, TransactionsByCategoryAndMonth,\
    TransactionsCategoriesSummarybyMonth, ExpensesSummarybyMonth, MonthlyBalance, MonthlyCategoriesBalance


urlpatterns = [
    # lista de transacciones por mes, usa date_month
    path('', TransactionsByMonth.as_view()),
    path('expenses/summary/', ExpensesSummarybyMonth.as_view()),
    path('summary/', TransactionsCategoriesSummarybyMonth.as_view()),
    path('balance/', MonthlyBalance.as_view()),
    path('categories/<str:category>/', TransactionsByCategoryAndMonth.as_view()),
    path('balance/category/<str:category>/', MonthlyCategoriesBalance.as_view()),
    path('<str:transaction_id>/', TransactionDetail.as_view())
]
