from django.contrib import admin

from .models import Recipe, Water, Malt, Hop

class WaterInline(admin.TabularInline):
    model = Water
    extra = 0

class MaltInline(admin.TabularInline):
    model = Malt
    extra = 0

class HopInline(admin.TabularInline):
    model = Hop
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Beer information', {'fields': ['name', 'beer_type']})
    ]
    inlines = [WaterInline, MaltInline, HopInline]

admin.site.register(Recipe, RecipeAdmin)
