from django.urls import path
from . import views

app_name = "budget"
urlpatterns = [
    path('',views.BudgetList.as_view()),
    path('<str:pk>/', views.BudgetDetail.as_view()),
]