from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductListView, ContactInfoView, BaseView, ProductDetailView, BlogCreateView, BlogListView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    VersionCreateView, VersionListView, VersionUpdateView, VersionDeleteView, VersionDetailView, CategoryListView

urlpatterns = [
    path("", ProductListView.as_view(), name='index'),
    path("contact_info", ContactInfoView.as_view()),
    path('base', BaseView.as_view()),
    path('product_detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('catalog/product_create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/product_update', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/product_delete', ProductDeleteView.as_view(), name='product_delete'),
    path('catalog/blog_create', BlogCreateView.as_view(), name='blogs_create'),
    path('catalog/blog_list', BlogListView.as_view(), name='blog_list'),
    path('catalog/blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('catalog/<int:pk>/update', BlogUpdateView.as_view(), name='blog_update'),
    path('catalog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
    path('catalog/version_create', VersionCreateView.as_view(), name='version_create'),
    path('catalog/version_list', VersionListView.as_view(), name='version_list'),
    path('catalog/<int:pk>/version_update', VersionUpdateView.as_view(), name='version_update'),
    path('catalog/<int:pk>/version_delete', VersionDeleteView.as_view(), name='version_delete'),
    path('catalog/<int:pk>/version_detail', VersionDetailView.as_view(), name='version_detail'),
    path('catalog/category_list', CategoryListView.as_view(), name='category_list'),

]
