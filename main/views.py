from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

   


    context: dict = {
        'title': 'Drev',
        'content': 'Магазин мебели - DREV',
      
        
    }

    return render(request, 'main/index.html', context)


def about(request):
    context: dict = {
        'title': 'Drev - о нас',
        'content': 'О нас',
        'text_on_page': "все про магазин."
        
    }

    return render(request, 'main/about.html', context)


