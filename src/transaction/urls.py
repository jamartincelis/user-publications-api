from django.urls import path, include

from transaction.views import TransactionsByMonth, TransactionDetail, TransactionsByCategoryAndMonth,\
    TransactionsCategoriesSummarybyMonth, ExpensesSummarybyMonth, MonthlyBalance, MonthlyCategoriesBalance


urlpatterns = [
    # lista de transacciones por mes, usa date_month
    path('', TransactionsByMonth.as_view()),
    # da un resumen de gastos mensuales organizados por categoría
    path('expenses/summary/', ExpensesSummarybyMonth.as_view()),
    # Regresa un resumen de las transacciones por categoría en un mes en específico
    path('summary/', TransactionsCategoriesSummarybyMonth.as_view()),
    # regresa el balance mensual con de los último n meses según la variable de entorno
    path('balance/', MonthlyBalance.as_view()),
    path('categories/<str:category>/', TransactionsByCategoryAndMonth.as_view()),
    path('balance/category/<str:category>/', MonthlyCategoriesBalance.as_view()),
    # Detalle de la transacción
    path('<str:pk>/', TransactionDetail.as_view())
]
