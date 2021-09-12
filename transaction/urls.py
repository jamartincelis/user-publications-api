from django.urls import path
from . import views

app_name = "transaction"
urlpatterns = [
    path('', views.TransactionList.as_view()),
    path('<str:pk>/', views.TransactionDetail.as_view()),
]