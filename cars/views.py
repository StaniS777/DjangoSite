from django.shortcuts import render, redirect
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView,
)
from django.urls import reverse_lazy

from cars.forms import CarCreateUpdateForm
from cars.models import Car

class CarListView(ListView):
    model = Car
    template_name = "cars_list.html"
    

class CarCreateView(CreateView):
    template_name = "cars_create.html"
    model = Car
    form_class = CarCreateUpdateForm
    success_url = reverse_lazy("cars_list")



class CarUpdateView(UpdateView):
    template_name = "cars_create.html"
    model = Car
    form_class = CarCreateUpdateForm
    success_url = reverse_lazy("cars_list")

