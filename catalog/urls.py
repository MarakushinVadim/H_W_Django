from django.urls import path

from catalog.views import index, contact_info

urlpatterns = [path("", index), path("contact_info", contact_info)]
