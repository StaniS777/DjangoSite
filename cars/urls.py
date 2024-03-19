from django.urls import path
# from cars.views import cars_list, cars_create
from cars.views import CarsListView, CarCreateView

# urlpatterns = [
#     path("", cars_list, name='cars_list'),
#     path("add_car", cars_create, name='cars_create'),
# ]


urlpatterns = [
    path("", CarsListView.as_view(), name='cars_list'),
    path("add_car", CarCreateView.as_view(), name='cars_create'),
]
