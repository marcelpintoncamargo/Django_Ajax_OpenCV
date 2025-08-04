from django.urls import path
from . import views

urlpatterns = [
    ## ******** FIRST CASE OF IMAGE ANALYSIS !!! *************
    # http://127.0.0.1:8000/image_analysis_01_path
    path('image_analysis_01_path', views.image_analysis_01_function, name="image_analysis_01_name"),
]
