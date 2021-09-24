from django.urls import path

from account.views import AccountDetail, CreateAccountView


app_name = "user"

urlpatterns = [
    path('', CreateAccountView.as_view()),
    path('<str:pk>/', AccountDetail.as_view()),
]
