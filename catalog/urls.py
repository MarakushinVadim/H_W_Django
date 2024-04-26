from django.urls import path

from catalog.views import index, contact_info, base, product_detail

urlpatterns = [
    path("", index, name='index'),
    path("contact_info", contact_info),
    path('base', base),
    path('product_detail/<int:pk>/', product_detail, name='product_detail')
]
