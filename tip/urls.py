from django.urls import path
from . import views

app_name = "tip"

urlpatterns = [
    path('', views.TipList.as_view()),
]
