from django.http import HttpResponse
from django.shortcuts import render

from recipes.models import Recipe

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes_list': recipes})
