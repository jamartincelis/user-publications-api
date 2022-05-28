from django.urls import path

from faq.views import FaqList


urlpatterns = [
    path('', FaqList.as_view()),
]
