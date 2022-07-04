from django.urls import path, include

urlpatterns = [
    path('api/weather/', include('weather.urls')),
]
