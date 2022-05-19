from django.contrib import admin
from django.urls import path, include

from transaction.views import NewTransaction


urlpatterns = [
    path('admin/', admin.site.urls),
    path('monitoring/', include('monitoring.urls')),
    path('users/<str:user>/budgets/', include('budget.urls')),
    path('users/<str:user>/transactions/', include('transaction.urls')),
    path('new-transaction/', NewTransaction.as_view()),
    path('faqs/', include('faq.urls')),
    path('tips/', include('tip.urls')),
    path('notifications/', include('notification.urls')),    
]
