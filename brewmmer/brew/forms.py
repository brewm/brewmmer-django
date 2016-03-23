from django import forms

from models import Recipe

class CreateForm(forms.Form):
    brew_name = forms.CharField(label='Brew name', max_length=100)
    recipe = forms.ChoiceField(choices=[(r, r) for r in Recipe.objects.all()])

