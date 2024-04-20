from django.shortcuts import render


def index(request):
    return render(request, "catalog/index.html")


def contact_info(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(f"Имя - {name}")
        print(f"Номер телефона - {phone}")
        print(f"Сообщение - {message}")
    return render(request, "catalog/contact_info.html")
