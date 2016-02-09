from django.contrib import admin

from .models import Recipe, Water, Malt, Hop

admin.site.register(Recipe)
admin.site.register(Water)
admin.site.register(Malt)
admin.site.register(Hop)
