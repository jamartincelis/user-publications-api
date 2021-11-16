from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('user/', include('user.urls')),
    path('user/<str:user>/accounts/', include('account.urls')),
    path('user/<str:user>/budgets/', include('budget.urls')),
    path('user/<str:user>/transactions/', include('transaction.urls')),
    path('faqs/', include('faq.urls')),
    path('tips/', include('tip.urls')),
    path('notifications/', include('notification.urls')),
]
