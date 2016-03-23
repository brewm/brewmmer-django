from django.http import HttpResponse

from django.shortcuts import render

from models import Brew
from models import Recipe
from forms import CreateForm

def index(request):
  return HttpResponse("First view of Brew")

def create(request):
  return render(request, "brew/create.html", {"form":CreateForm})

def api(request):
  if request.method == "POST":
    Brew.objects.create(name=request.POST['brew_name'], recipe=Recipe.objects.get(name=request.POST['recipe']))
    return HttpResponse("SUCCESS")
