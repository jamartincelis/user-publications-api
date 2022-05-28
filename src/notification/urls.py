from django.urls import path

from notification.views import NoticationList


urlpatterns = [
    path('', NoticationList.as_view()),
]
