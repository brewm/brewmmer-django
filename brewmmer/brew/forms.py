from django import forms
from django.forms import ModelForm

from models import Recipe, Brew, MashIngredient, MashStep, BoilIngredient, BoilStep, Malt, Water, Hop

class CreateForm(forms.Form):
    brew_name = forms.CharField(label='Brew name', max_length=100)
    recipe = forms.ChoiceField(choices=[(r, r) for r in Recipe.objects.all()])