from django.urls import path

from user.views import UserDetail, CreateUserView


urlpatterns = [
    path('', CreateUserView.as_view()),
    path('<str:pk>/', UserDetail.as_view()),
]
