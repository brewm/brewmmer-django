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
    def mash_steps(self):
        return MashStep.objects.filter(brew=self)
    @property
    def boil_steps(self):
        return BoilStep.objects.filter(brew=self) 

class MashStep(models.Model):
    brew = models.ForeignKey(Brew, on_delete=models.CASCADE)
    duration = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    @property
    def ingredients(self):
        return MashIngredient.objects.filter(mash_step=self)

class MashIngredient(models.Model):
    mash_step = models.ForeignKey(MashStep, on_delete=models.CASCADE)
    name =  models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

class BoilStep(models.Model):
    brew = models.ForeignKey(Brew, on_delete=models.CASCADE)
    duration = models.DecimalField(max_digits=5, decimal_places=2)
    @property
    def ingredients(self):
        return BoilIngredient.objects.filter(boil_step=self)

class BoilIngredient(models.Model):
    boil_step = models.ForeignKey(BoilStep, on_delete=models.CASCADE)
    name =  models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=5, decimal_places=2)