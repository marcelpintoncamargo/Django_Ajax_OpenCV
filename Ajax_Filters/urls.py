from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/filters_path_02
    path('filters_path_02', views.filters_02_function, name="filters_02_name"),

    # http://127.0.0.1:8000/filters_path_03
    path('filters_path_03', views.filters_03_function, name="filters_03_name"),
]
