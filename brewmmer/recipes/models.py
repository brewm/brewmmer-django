from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    beer_type = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Water(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    volume = models.DecimalField(max_digits=5, decimal_places=2)

class Malt(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

class Hop(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
