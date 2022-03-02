from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pfm-service/monitoring/', include('monitoring.urls')),
    path('pfm-service/user/<str:user>/budgets/', include('budget.urls')),
    path('pfm-service/user/<str:user>/transactions/', include('transaction.urls')),
]
