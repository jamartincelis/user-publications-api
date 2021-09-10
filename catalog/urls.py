from catalog.models import Code
from django.urls import path

from catalog.views import CodeTypeList, CodeList, CatalogList, Catalog

app_name = "catalog"
urlpatterns = [
    path('codetypes_list/', CodeTypeList.as_view()),
    path('codes_list/', CodeList.as_view()),
    path('list/', CatalogList.as_view()),
    path('<str:name>/', Catalog.as_view()),
]
