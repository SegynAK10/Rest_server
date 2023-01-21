from django.shortcuts import render


# Create your views here.
def index_page(request):
    contex = {
        'title': 'MAIN'
    }
    return render(request, 'index.html', contex)
