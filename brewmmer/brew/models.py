from django.db import models


class Brew(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField('started date')
    end_time = models.DateTimeField('finished date')
