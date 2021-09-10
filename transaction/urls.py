from django.urls import path
from . import views

app_name = "transaction"
urlpatterns = [
    path('', views.TransactionList.as_view(), name='budgets'),
    path('<int:pk>/', views.TransactionDetail.as_view()),
]