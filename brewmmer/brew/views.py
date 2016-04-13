from django.http import HttpResponse

from django.shortcuts import render

from models import Brew, Recipe, BoilIngredient, BoilStep, MashIngredient, MashStep
from forms import CreateForm, MashStepFormSet

from django.http import HttpResponseRedirect
from django.views.generic import CreateView


def index(request):
  return HttpResponse("First view of Brew")

def create(request):
	create_form = CreateForm()
  	return render(request, "brew/create.html", {"form":create_form})

def api(request, brew_id=None):
  if request.method == "POST":
    brew = Brew.objects.create(name=request.POST['brew_name'], recipe=Recipe.objects.get(name=request.POST['recipe']))
    
    mash_step = MashStep.objects.create(brew=brew, duration=request.POST['mash_duration'], temperature=request.POST['temperature'])
    
    water_ing = MashIngredient.objects.create(mash_step=mash_step, name=request.POST['water'], amount=request.POST['water_volume'])
    malt_ing = MashIngredient.objects.create(mash_step=mash_step, name=request.POST['malt'], amount=request.POST['malt_weight'])
    
    boil_step = BoilStep.objects.create(brew=brew, duration=request.POST['boil_duration'])
    hop_ing = BoilIngredient.objects.create(boil_step=boil_step, name=request.POST['hop'], amount=request.POST['hop_weight'])
    return HttpResponse("SUCCESS")
  if request.method == "GET":
    try:
      brew = Brew.objects.get(id=brew_id)
      return render(request, "brew/details.html", {"brew":brew})
    except Brew.DoesNotExist:
      return HttpResponse("No brew found with this ID: %s" % brew_id)


def list(request):
  brews = Brew.objects.all()
  return render(request, "brew/list.html", {"brew_list":brews})


#class BrewCreateView(CreateView):
#	template_name = 'brew_add.html'
#	model = Brew
#	form_class = CreateForm
#	success_url = 'success/'
#	
#	def get(self, request, *args, **kwargs):
#		self.object = None
#		form_class = self.get_form_class()
#		form = self.get_form(form_class)
#		mashstep_form = MashStepFormSet()
#		return self.render_to_response(self.get_context_data(form=form, mashstep_form=mashstep_form))
#
#	def post(self, request, *args, **kwargs):
#		self.object = None
#		form_class = self.get_form_class()
#		form = self.get_form(form_class)
#		mashstep_form = MashStepFormSet(self.request.POST)
#		if (form.is_valid() and mashstep_form.is_valid()):
#			return self.form_valid(form, mashstep_form)
#		else:
#			return self.form_invalid(form, mashstep_form)
#
#	def form_valid(self, form, mashstep_form):
#		self.object = form.save()
#		mashstep_form.instance = self.object
#		mashstep_form.save()
#		return HttpResponseRedirect(self.get_success_url())
#
#	def form_invalid(self, form, mashstep_form):
#		return self.render_to_response(
#			self.get_context_data(form=form,
#				mashstep_form=mashstep_form))
#
#
#
#
#