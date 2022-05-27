from django.urls import path

from catalog.views import CatalogListApiView, CatalogApiView, ItemDetail


urlpatterns = [
    # todos los catálogos
    path('all/', CatalogListApiView.as_view()),
    # un objeto del tipo item únicamente
    path('items/<str:pk>/', ItemDetail.as_view()),
    # un arreglo de catálogos con sus respectivos items filtrados con queryparams
    path('', CatalogApiView.as_view()),
]
