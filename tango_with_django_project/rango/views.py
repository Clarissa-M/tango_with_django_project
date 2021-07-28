from django.shortcuts import render
from rango.models import Category

from django.http import HttpResponse

def index(request):
    #list of all categorie currently stored, ordered by number of likes (descending) retrieve top 5
    category_list = Category.objects.order_by('-likes')[:5]
    
    context_dict = {}
    context_dict={'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    context_dict['categories'] = category_list #place list in context dictionary
   
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')