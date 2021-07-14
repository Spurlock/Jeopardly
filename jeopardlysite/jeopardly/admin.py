from django.contrib import admin

from .models import RawCategory, Category, Clue

admin.site.register(RawCategory)
admin.site.register(Category)
admin.site.register(Clue)