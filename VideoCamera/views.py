from django.shortcuts import render
import cv2
import threading
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np

@gzip.gzip_page
def videocamera_function(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type = "multipart/x-mixed-replace; boundary=frame")

        # response = StreamingHttpResponse(gen(cam), content_type = "multipart/x-mixed-replace; boundary=frame")
        # return render(request, 'VideoCamera/videocamera_01.html', {'video': response})
    except:
        pass
    return render(request, 'VideoCamera/videocamera_01.html')

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.video.set(cv2.CAP_PROP_FOURCC, 0x32595559)
        self.video.set(cv2.CAP_PROP_FPS, 25)

        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target = self.update, args = ()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, jpeg = cv2.imencode('.jpg', gray)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield   (b'--frame\r\n'
                 b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



## *************************************************************************************
def videocamera_render_function(request):
    return render(request, 'VideoCamera/videocamera_01.html')


## Function activated by AJAX POST from  --> VideoCamera/videocamera_01.html, requesting the data !! 
## The info also is displayed as json in --> http://127.0.0.1:8000/videocamera_path/ajax_video_camera_image_path
@csrf_exempt
def ajax_video_camera_image_function(request):
    results = {}
    if request.accepts("application/json"):
        try:
            capture = cv2.VideoCapture(0, cv2.CAP_DSHOW);
            ret, frame = capture.read();
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
            _, jpeg = cv2.imencode('.jpg', gray);
            capture.release();
            ## cv2.destroyAllWindows()
            
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB);

            first_channel = rgb_image[:,:,0]
            second_channel = rgb_image[:, :, 1]
            third_channel = rgb_image[:, :, 2]

            first_channel_1D = np.ravel(first_channel)
            second_channel_1D = np.ravel(second_channel)
            third_channel_1D = np.ravel(third_channel)

            first_channel_1D_list = first_channel_1D.tolist()
            second_channel_1D_list = second_channel_1D.tolist()
            third_channel_1D_list = third_channel_1D.tolist()

            results["red_channel"] = first_channel_1D_list
            results["green_channel"] = second_channel_1D_list
            results["blue_channel"] = third_channel_1D_list

            return HttpResponse(json.dumps(results), content_type='application/json')

        except:
            pass
    else:
        print('not found')
        results = 'Not Ajax'
    return JsonResponse({'results': results})


def videocamera_render_02_function(request):
    return render(request, 'VideoCamera/videocamera_02.html')




