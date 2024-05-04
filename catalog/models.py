from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите название категории"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории", **NULLABLE
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название", help_text="Введите название продукта"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание продукта"
    )
    photo = models.ImageField(
        upload_to="media", **NULLABLE, verbose_name="Фото продукта"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Категория продукта",
        related_name="category",
    )
    price = models.CharField(
        max_length=100, **NULLABLE, verbose_name="Цена", help_text="Введите цену"
    )
    created_at = models.DateField(verbose_name="Дата создания записи", **NULLABLE)
    updated_at = models.DateField(verbose_name="Дата последнего изменения", **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок', help_text='Введите заголовок')
    slug = models.CharField(max_length=150, verbose_name='Slug', help_text='Введите Slug')
    content = models.TextField(verbose_name="Содержимое", help_text="Введите содержимое")
    preview = models.ImageField(upload_to="media", **NULLABLE, verbose_name="Превью")
    create_at = models.DateField(verbose_name="Дата создания записи", **NULLABLE)
    is_published = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0, **NULLABLE)

    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'