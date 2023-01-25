from django.shortcuts import render


# Create your views here.
def привет(request):
    context = {
        'title': 'store',
        'promo': True,
    }
    return render(request, 'привет.html', context)
