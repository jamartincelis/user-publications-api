from django.urls import path, include

from transaction.views import NewTransaction


urlpatterns = [
    path('pfm-service/monitoring/', include('monitoring.urls')),
    path('pfm-service/users/<str:user_id>/budgets/', include('budget.urls')),
    path('pfm-service/users/<str:user_id>/transactions/', include('transaction.urls')),
    path('pfm-service/new-transaction/', NewTransaction.as_view()),
    path('pfm-service/faqs/', include('faq.urls')),
    path('pfm-service/tips/', include('tip.urls')),
    path('pfm-service/notifications/', include('notification.urls')),
    path('pfm-service/catalogs/', include('catalog.urls')),
]
