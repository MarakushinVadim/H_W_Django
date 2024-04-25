import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        category_list = []
        with open(
            "catalog/management/commands/catalog_data.json", encoding="UTF-16"
        ) as file:
            category = json.load(file)
            for unit in category:
                if unit["model"] == "catalog.category":
                    category_list.append(unit)
        return category_list

    @staticmethod
    def json_read_products():
        product_list = []
        with open(
            "catalog/management/commands/catalog_data.json", encoding="UTF-16"
        ) as file:
            category = json.load(file)
            for unit in category:
                if unit["model"] == "catalog.product":
                    product_list.append(unit)
        return product_list

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    id=category["pk"],
                    name=category["fields"]["name"],
                    description=category["fields"]["name"],
                )
            )
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    id=product["pk"],
                    name=product["fields"]["name"],
                    description=product["fields"]["description"],
                    photo=product["fields"]["photo"],
                    category=Category.objects.get(pk=product["fields"]["category"]),
                    price=product["fields"]["price"],
                )
            )
        Product.objects.bulk_create(product_for_create)
