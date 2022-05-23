from django.urls import path, include

from transaction.views import NewTransaction


urlpatterns = [
    path('monitoring/', include('monitoring.urls')),
    path('users/<str:user_id>/budgets/', include('budget.urls')),
    path('users/<str:user_id>/transactions/', include('transaction.urls')),
    path('new-transaction/', NewTransaction.as_view()),
    path('faqs/', include('faq.urls')),
    path('tips/', include('tip.urls')),
    path('notifications/', include('notification.urls')),
    path('catalogs/', include('catalog.urls')),
]
