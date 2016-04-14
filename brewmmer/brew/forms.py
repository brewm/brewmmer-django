from django import forms
from django.forms import ModelForm

from models import Recipe, Brew, MashIngredient, MashStep, BoilIngredient, BoilStep, Malt, Water, Hop

class CreateForm(forms.Form):
    brew_name = forms.CharField(label='Brew name', max_length=100)
    recipe = forms.ChoiceField(choices=[(r, r) for r in Recipe.objects.all()])
    
    water = forms.ChoiceField(choices=[(w, w) for w in Water.objects.all()])
    water_volume = forms.DecimalField(max_digits=5, decimal_places=2)
    
    malt = forms.ChoiceField(choices=[(m, m) for m in Malt.objects.all()])
    malt_weight = forms.DecimalField(max_digits=5, decimal_places=2)
    
    mash_duration = forms.DecimalField(max_digits=5, decimal_places=2)
    temperature = forms.DecimalField(max_digits=5, decimal_places=2)
    
    hop = forms.ChoiceField(choices=[(m, m) for m in Hop.objects.all()])
    hop_weight = forms.DecimalField(max_digits=5, decimal_places=2)
    
    boil_duration = forms.DecimalField(max_digits=5, decimal_places=2)

    def __init__(self, *args, **kwargs):
    	super(CreateForm, self).__init__(*args, **kwargs)
    	self.fields['recipe'].choices = [(r, r) for r in Recipe.objects.all()]
    	self.fields['water'].choices = [(r, r) for r in Water.objects.all()]
    	self.fields['malt'].choices = [(r, r) for r in Malt.objects.all()]
    	self.fields['hop'].choices = [(r, r) for r in Hop.objects.all()]