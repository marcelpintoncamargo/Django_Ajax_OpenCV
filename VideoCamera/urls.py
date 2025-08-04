from django.urls import path
from . import views

urlpatterns = [

## ********* First case --> Capture Photos from VideoCamera, Image filter and save ... ************
    # http://127.0.0.1:8000/videocamera_path/render_path
    # Render the html page !
    path('render_path', views.videocamera_render_function, name = "videocamera_render_name"),


    # http://127.0.0.1:8000/videocamera_path/ajax_video_camera_image_path
    ## Ajax communication video camera image
    path('ajax_video_camera_image_path', views.ajax_video_camera_image_function, name = "ajax_video_camera_image_name"),

## ******* First case video camera ... *************
    #http://127.0.0.1:8000/videocamera_path
    # Send information from video camera
    path('', views.videocamera_function, name = "videocamera_name"),

## ****** Second case video camera ...  **********
    # http://127.0.0.1:8000/videocamera_path/render_02_path
    # Render the html page !
    path('render_02_path', views.videocamera_render_02_function, name = "videocamera_render_02_name"),


            
]