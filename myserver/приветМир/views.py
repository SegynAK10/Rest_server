from django.shortcuts import render
from приветМир.models import TestCat, Product


def привет(request):
    context = {
        'title': 'store',
        'promo': True,
        'categorys': TestCat.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'привет.html', context)
