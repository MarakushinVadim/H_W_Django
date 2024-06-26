from django.contrib import admin

from catalog.models import Category, Product, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "price",
        "category",
    )
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'content',
        'preview',
        'create_at',
        'is_published',
        'views_count'
    )


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'version_number',
        'version_name',
        'is_current'
    )
