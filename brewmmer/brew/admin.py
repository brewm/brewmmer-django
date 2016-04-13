from django.contrib import admin
from .models import Brew, MashStep

class BrewAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Brew information', {'fields': ['name', 'recipe']})
    ]

admin.site.register(Brew, BrewAdmin)
