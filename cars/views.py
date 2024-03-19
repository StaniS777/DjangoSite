from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.views.generic import ListView, CreateView
from django.urls import reverse

from cars.forms import CarCreateForm
from cars.models import Car

class CarsListView(ListView):
    template_name = "cars_list.html"
    model = Car

class CarCreateView(CreateView):
    template_name = "cars_create.html"
    model = Car
    form_class = CarCreateForm
    success_url = reverse("cars_list")


# def cars_list(request):
#     cars_list = Car.objects.all()
#     context = {
#         "cars_list": cars_list,
#     }
#     return render(
#         request, 
#         "cars_list.html",
#         context,

#     )

# def cars_create(request: HttpRequest):
#     form = CarCreateForm(request.POST)
    
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('/cars')

#     return render(
#         request, 
#         "cars_create.html",
#         {"form": form},
#     )
