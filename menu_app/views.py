from django.shortcuts import render
from .models import Category, Dish


def base(request):
    categories = Category.objects.all()
    return render(request, 'menu_app/base.html', {'title': 'Категории', 'categories': categories})


def index(request):
    dishes = Dish.objects.all()
    return render(request, 'menu_app/index.html',  {'dishes': dishes})


def get_id(request, pk):
    categories = Category.objects.get(id=pk).dishes.all()
    return render(request, 'menu_app/category.html',  {'categories': categories})

