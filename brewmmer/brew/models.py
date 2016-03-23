from django.db import models
from smart_selects.db_fields import GroupedForeignKey 
from smart_selects.db_fields import ChainedForeignKey 

from decimal import Decimal

import datetime

from recipes.models import Recipe, Water, Malt, Hop

class Brew(models.Model):
    name = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    @property
    def mash_step(self):
        return MashStep.objects.filter(brew=self)
    @property
    def boil_step(self):
        return BoilStep.objects.filter(brew=self)    

class MashStep(models.Model):
    brew = models.ForeignKey(Brew, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DecimalField(max_digits=5, decimal_places=2)
    @property
    def water(self):
        return WaterIngredient.objects.filter(brew=self) 
    @property
    def malt(self):
        return MaltIngredient.objects.filter(brew=self)

class WaterIngredient(models.Model):
    mash_step = models.ForeignKey(MashStep, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    water = ChainedForeignKey(
        Water, 
        chained_field="recipe",
        chained_model_field="recipe", 
        show_all=False, 
        auto_choose=True
    )
    water_volume = models.DecimalField(max_digits=5, decimal_places=2)

class MaltIngredient(models.Model):
    mash_step = models.ForeignKey(MashStep, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    Malt = ChainedForeignKey(
        Malt, 
        chained_field="recipe",
        chained_model_field="recipe", 
        show_all=False, 
        auto_choose=True
    )
    malt_weight = models.DecimalField(max_digits=5, decimal_places=2)

class BoilStep(models.Model):
    brew = models.ForeignKey(Brew, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    hop = ChainedForeignKey(
        Hop, 
        chained_field="recipe",
        chained_model_field="recipe", 
        show_all=False, 
        auto_choose=True
    )
    hop_weight = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DecimalField(max_digits=5, decimal_places=2)
