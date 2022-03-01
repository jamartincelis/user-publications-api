from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<str:user>/budgets/', include('budget.urls')),
    path('user/<str:user>/transactions/', include('transaction.urls')),
]
