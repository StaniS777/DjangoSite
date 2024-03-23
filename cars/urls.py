from django.urls import path
from cars.views import (
    CarListView, 
    CarCreateView, 
    CarUpdateView,
)


urlpatterns = [
    path("", CarListView.as_view(), name='cars_list'),
    path("add_car", CarCreateView.as_view(), name='cars_create'),
    path("<int:pk>/update", CarUpdateView.as_view(), name='cars_update'),
]
