from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def contact_info(request):
    return render(request, 'catalog/contact_info.html')
