from django.urls import path

from monitoring.views import HealthCheckApiView, SentryApiView


urlpatterns = [
    path('health-check/', HealthCheckApiView.as_view(), name="health-check"),
    path('sentry/', SentryApiView.as_view(), name="sentry"),
]
