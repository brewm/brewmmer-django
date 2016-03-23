from django.contrib import admin
import nested_admin
from .models import Brew, MashStep, WaterIngredient, MaltIngredient, BoilStep

class WaterIngredientInline(nested_admin.NestedStackedInline):
    model = WaterIngredient
    extra = 1

class MaltIngredientInline(nested_admin.NestedStackedInline):
    model = MaltIngredient
    extra = 1

class MashStepInline(nested_admin.NestedStackedInline):
    model = MashStep
    extra = 2
    inlines = [WaterIngredientInline, MaltIngredientInline]

class BoilStepInline(nested_admin.NestedStackedInline):
    model = BoilStep
    extra = 2

class BrewAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        ('Brew information', {'fields': ['name', 'recipe']})
    ]
    inlines = [MashStepInline, BoilStepInline]

admin.site.register(Brew, BrewAdmin)
