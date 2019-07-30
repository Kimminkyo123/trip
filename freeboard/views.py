from django.shortcuts import render
from .models import Freeboard
from django.views.generic import ListView, DetailView

class BoardLV(ListView):
    model= Freeboard

class BoardDV(DetailView):
    model = Freeboard