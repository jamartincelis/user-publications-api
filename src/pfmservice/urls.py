from django.contrib import admin
from django.urls import path, include

from transaction.views import NewTransaction


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pfm-service/monitoring/', include('monitoring.urls')),
    path('pfm-service/users/<str:user>/budgets/', include('budget.urls')),
    path('pfm-service/users/<str:user>/transactions/', include('transaction.urls')),
    path('pfm-service/new-transaction/', NewTransaction.as_view()),
    path('pfm-service/faqs/', include('faq.urls')),
    path('pfm-service/tips/', include('tip.urls')),
    path('pfm-service/notifications/', include('notification.urls')),    
]
