from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):

   # Construct a dictionary to pass to the template engine as its context.
   # Note the key boldmessage is the same as {{boldmessage}} in the template!
 
   category_list = Category.objects.order_by('-likes')[:5]
   page_list = Page.objects.order_by('-views')[:5]
   context_dict = {'pages':page_list, 'categories':category_list}

   return render(request, 'rango/index.html', context_dict)

def about(request):
   context_dict = {'boldmessage':'This tutorial has been put together by <Jaroslav Sak>'}
   return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
   context_dict = {}

   try:
      category = Category.objects.get(slug=category_name_slug)
      pages = Page.objects.filter(category=category)
      context_dict['pages'] = pages
      context_dict['category'] = category
   except Category.DoesNotExist:
      context_dict['pages'] = None
      context_dict['category'] = None
      
   return render(request, 'rango/category.html', context_dict)
      
# Create your views here.
