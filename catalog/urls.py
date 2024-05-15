from django.urls import path

from catalog.views import ProductListView, ContactInfoView, BaseView, ProductDetailView, BlogCreateView, BlogListView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path("", ProductListView.as_view(), name='index'),
    path("contact_info", ContactInfoView.as_view()),
    path('base', BaseView.as_view()),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/product_create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/product_update', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/product_delete', ProductDeleteView.as_view(), name='product_delete'),
    path('catalog/blog_create', BlogCreateView.as_view(), name='blogs_create'),
    path('catalog/blog_list', BlogListView.as_view(), name='blog_list'),
    path('catalog/blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('catalog/<int:pk>/update', BlogUpdateView.as_view(), name='blog_update'),
    path('catalog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete')

]
