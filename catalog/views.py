from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def index(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, "catalog/index.html", context)


def contact_info(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(f"Имя - {name}")
        print(f"Номер телефона - {phone}")
        print(f"Сообщение - {message}")
    return render(request, "catalog/contact_info.html")


def base(request):
    return render(request, 'base.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product_detail.html', context)
