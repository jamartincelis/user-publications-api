from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('<str:pk>/', views.UserDetail.as_view()),
]