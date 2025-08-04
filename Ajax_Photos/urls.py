from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_function, name = "index_name"),
    path('photo_add_path', views.photo_add_function, name  = "photo_add_name" ),
]