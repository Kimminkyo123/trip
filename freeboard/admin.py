from django.contrib import admin
from .models import Freeboard
from .models import Star

class Freeboardinline(admin.StackedInline):
    model = Freeboard
    extra = 0

class Staradmin(admin.ModelAdmin):
    inlines =[Freeboardinline]
    list_display = ('name','body')




    
admin.site.register(Star, Staradmin)
admin.site.register(Freeboard)

