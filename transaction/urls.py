from django.urls import path
from . import views

app_name = "transaction"
urlpatterns = [
    path('', views.transaction_list),
    path('<str:pk>/', views.TransactionDetail.as_view()),
]