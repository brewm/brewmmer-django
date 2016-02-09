from django.db import models
import datetime

from recipes.models import Recipe

class Brew(models.Model):
    name = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    start_time = models.DateTimeField('started date')
    end_time = models.DateTimeField('finished date')
