from django.http import HttpResponse

from django.shortcuts import render

from models import Brew, Recipe, BoilIngredient, BoilStep, MashIngredient, MashStep
from forms import CreateForm

from django.http import HttpResponseRedirect
from django.views.generic import CreateView

import json

def get_or_none(klass, object_id):
    o = None
    try:
        o = klass.objects.get(id=object_id)
    except:
        pass
    return o

def index(request):
  return HttpResponse("First view of Brew")

def error(request):
  return render(request, "brew/error.html")

def create(request):
  import pdb; pdb.set_trace()
  create_form = CreateForm()
  return render(request, "brew/create.html", {"form":create_form})

def api(request, brew_id=None):
  if request.method == "POST":
    brew = Brew.objects.create(name=request.POST['brew_name'], recipe=Recipe.objects.get(name=request.POST['recipe']))
    return render(request, "brew/create_mash_steps.html", {"brew": brew})
  if request.method == "GET":
    try:
      brew = Brew.objects.get(id=brew_id)
      return render(request, "brew/details.html", {"brew":brew})
    except Brew.DoesNotExist:
      return HttpResponse("No brew found with this ID: %s" % brew_id)

"""
{
    "steps": [
        {
            "brew": 1,
            "duration": 10,
            "temperature" 10,
            "ingredient": [
                {
                    "name": "water",
                    "amount": 10
                },
                {
                    "name": "malt",
                    "amount": 10
                }
            ]
        }
    ]
}

    mash_step = MashStep.objects.create(brew=brew, duration=request.POST['mash_duration'], temperature=request.POST['temperature'])
    
    water_ing = MashIngredient.objects.create(mash_step=mash_step, name=request.POST['water'], amount=request.POST['water_volume'])
    malt_ing = MashIngredient.objects.create(mash_step=mash_step, name=request.POST['malt'], amount=request.POST['malt_weight'])
    
    boil_step = BoilStep.objects.create(brew=brew, duration=request.POST['boil_duration'])
    hop_ing = BoilIngredient.objects.create(boil_step=boil_step, name=request.POST['hop'], amount=request.POST['hop_weight'])
"""
def create_mash(request):
  if request.method == "POST":
    steps = json.loads(request.POST['formdata'])['steps']
    brew = None
    for step in steps:
      brew_id = step['brew']
      brew = get_or_none(Brew, brew_id)
      if brew is None:
        return HttpResponse("/brew/error")
      duration = step['duration']
      temperature = step['temperature']
      mash_step = MashStep.objects.create(brew=brew, duration=duration, temperature=temperature)

      ingredients = step['ingredients']
      for ing in ingredients:
        name = ing['name']
        amount = ing['amount']
        # TODO: check if ingredient is from the recipe
        # https://docs.djangoproject.com/en/1.9/ref/models/querysets/#select-related
        ingredient = MashIngredient.objects.create(mash_step=mash_step, name=name, amount=amount)
    return HttpResponse("/brew/create-boil?brew={}".format(brew_id))
  if request.method == "GET":
    return render(request, "brew/create_mash_steps.html")

def create_boil(request):
  if request.method == "POST":
    steps = json.loads(request.POST['formdata'])['steps']
    brew = None
    for step in steps:
      brew_id = step['brew']
      brew = get_or_none(Brew, brew_id)
      if brew is None:
        return HttpResponse("/brew/error")
      duration = step['duration']
      boil_step = BoilStep.objects.create(brew=brew, duration=duration)

      ingredients = step['ingredients']
      for ing in ingredients:
        name = ing['name']
        amount = ing['amount']
        # TODO: check if ingredient is from the recipe
        # https://docs.djangoproject.com/en/1.9/ref/models/querysets/#select-related
        ingredient = BoilIngredient.objects.create(boil_step=boil_step, name=name, amount=amount)
    return HttpResponse("/brew/%s" % brew_id)
  if request.method == "GET":
    brew_id = request.GET['brew']
    return render(request, "brew/create_boil_steps.html", {'brew':Brew.objects.get(id=brew_id)})

def list(request):
  brews = Brew.objects.all()
  return render(request, "brew/list.html", {"brew_list":brews})