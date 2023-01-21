from django.shortcuts import render


# Create your views here.
def привет(request):
    return render(request, 'привет.html', {'title': 'Привет Тест'})
