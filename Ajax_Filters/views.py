from django.shortcuts import render
from django.http import  HttpResponse
from Ajax_Filters.models import  SaveImageModel
import json
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from django.core.files.base import ContentFile
import base64
import numpy
import io
from Ajax_Filters.image_filters import first_order_filter_function, second_order_filter_function
from Ajax_Filters.image_filters import blur_filter_function, threshold_filter_function, space_transformation_function


@csrf_exempt
def filters_02_function(request):
    print('In Filter Function')
    results = {}
    if request.accepts("application/json"):  ## This information came from main.js -->  ajax
        try:
            ##print('ola mundo')
            ##print(request.POST.get('image'))
            ##print('name: ' , request.POST.get('name'))
            ##print('description: ' , request.POST.get('description'))
            ##print('filter_class: ' , request.POST.get('filter_class'))
            ##print('filter_name: ' , request.POST.get('filter_name'))
            ##print('kernel_canny', request.POST.get('kernel_canny'))
            ##print('kernel_first_order', request.POST.get('kernel_first_order'))
            ##print('lim_inf_canny', request.POST.get('lim_inf_canny'))
            ##print('lim_sup_canny', request.POST.get('lim_sup_canny'))
            ##print('kernel_second_order', request.POST.get('kernel_second_order'))
            ##print('sigma_laplace_of_gaussian', request.POST.get('sigma_laplace_of_gaussian'))
            ##print('sharp_laplacian_w1', request.POST.get('sharp_laplacian_w1'))
            ##print('sharp_laplacian_w2', request.POST.get('sharp_laplacian_w2'))
            ##print('sharp_laplacian_alpha', request.POST.get('sharp_laplacian_alpha'))

            image_url = request.POST.get('image')
            name = request.POST.get('name')
            filter_class = request.POST.get('filter_class')
            filter_name = request.POST.get('filter_name')
            desccription = request.POST.get('description')
            ### First Order Filters
            kernel_canny = int(request.POST.get('kernel_canny'))
            kernel_first_order = int(request.POST.get('kernel_first_order'))
            lim_inf_canny = int(request.POST.get('lim_inf_canny'))
            lim_sup_canny = int(request.POST.get('lim_sup_canny'))
            ### Second Order Filters
            kernel_second_order = int(request.POST.get('kernel_second_order'))
            sigma_laplace_of_gaussian = float(request.POST.get('sigma_laplace_of_gaussian'))
            sharp_laplacian_w1 = float(request.POST.get('sharp_laplacian_w1'))
            sharp_laplacian_w2 = float(request.POST.get('sharp_laplacian_w2'))
            sharp_laplacian_alpha = float(request.POST.get('sharp_laplacian_alpha'))
            ### Blur Filters
            kernel_blur = int(request.POST.get('kernel_blur'))
            sigma_x_blur = float(request.POST.get('sigma_x_blur'))
            sigma_y_blur = float(request.POST.get('sigma_y_blur'))
            mean_filter_option = request.POST.get('mean_filter_option')
            ### Threshold Filters
            threshold_name = request.POST.get('threshold_name')
            threshold_value = int(request.POST.get('threshold_value'))
            threshold_max_value = int(request.POST.get('threshold_max_value'))

            print('type of image_url')
            print(type(image_url))  ## type: <class 'str'>
            format, imgstr = image_url.split(';base64,')
            ## format: data:image/jpeg 
            ## imgstr: string containing the data url 
            ## imgstr: --> type = <class 'str'> ; length = 169520

            ext = format.split('/')[-1]
            ## ext = jpeg

            ## data = ContentFile(base64.b64decode(imgstr), name='id_'+ str(index) + '.' + ext)
            ## ********** Save the image in the mmodel *********** ##

            decodedbytes = base64.decodebytes(str.encode(imgstr))
            image_stream = io.BytesIO(decodedbytes)
            image_input = Image.open(image_stream)
            ## decodedbytes: --> type = <class 'bytes'> ; length =  127138
            ## image_stream: <_io.BytesIO object at 0x000001E04AEFB540>
            ## image:  <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x480 at 0x1D1403C4D60>

            filetype = image_input.format
            ## filetype:  JPEG

            # convert the image to array and do some processing !!!
            array_img = numpy.array(image_input)

            print('max value: ', numpy.amax(image_input))
            print('min value: ', numpy.amin(image_input))
            print('Shape of image_input: ', numpy.shape(image_input));

            print('max value: ', numpy.amax(array_img))
            print('min value: ', numpy.amin(array_img))
            print('Shape of image_input: ', numpy.shape(array_img));

            ## *****  First Order Filters **************
            if filter_class == 'First Order Filters':
                print('First Order Filters')
                channel_01, channel_02, channel_03 = first_order_filter_function(array_img, filter_name,
                                                                                 kernel_first_order, lim_inf_canny,
                                                                                 lim_sup_canny, kernel_canny)

            ## !****  Second Order Filters **************
            elif filter_class == 'Second Order Filters':
                print('Second Order Filters')
                channel_01, channel_02, channel_03 = second_order_filter_function(array_img, filter_name,
                                                                                  kernel_second_order,
                                                                                  sigma_laplace_of_gaussian,
                                                                                  sharp_laplacian_w1,
                                                                                  sharp_laplacian_w2,
                                                                                  sharp_laplacian_alpha)

            ## ?****  Blur Filters **************
            elif filter_class == 'Blur Filters':
                print('Blur Filters')
                channel_01, channel_02, channel_03 = blur_filter_function(array_img, filter_name, kernel_blur,
                                                                          sigma_x_blur, sigma_y_blur,
                                                                          mean_filter_option)

            ## *****  Threshold Filters **************
            elif filter_class == 'Threshold Filters' and filter_name == 'Threshold':
                print('Threshold Filters')
                channel_01, channel_02, channel_03 = threshold_filter_function(array_img, threshold_name,
                                                                               threshold_value, threshold_max_value)


            ## !******* Space Transformation ********
            elif filter_class == 'Space Transformation':
                print('Space Transformation')
                channel_01, channel_02, channel_03 = space_transformation_function(array_img, filter_name)

            results["red_channel"] = channel_01
            results["green_channel"] = channel_02
            results["blue_channel"] = channel_03
            return HttpResponse(json.dumps(results), content_type='application/json')

        except:
            pass

    return render(request, 'Ajax_Filters_Photos/Ajax_Filters_Images_02.html')

@csrf_exempt
def filters_03_function(request):
    objects = SaveImageModel.objects.all().order_by('id')
    index = len(objects)
    if request.accepts("application/json"):
        try:
            print('Saving the image...')
            image_url = request.POST.get('image')
            print(type(image_url))  ## type: <class 'str'>
            format, imgstr = image_url.split(';base64,')
            ## format: data:image/jpeg
            ## imgstr: string containing the data url
            ext = format.split('/')[-1]
            ## ext = jpeg
            data = ContentFile(base64.b64decode(imgstr))
            file_name = str(request.POST.get('name')) + '_' + str(index) + '.' + ext

            ## ********** Save the image in the model *********** ##
            saverec = SaveImageModel()
            saverec.id = index ## json.loads(request.POST.get('id'))
            saverec.name = request.POST.get('name')
            saverec.description = request.POST.get('description')
            saverec.image.save(file_name, data, save=True)
            saverec.save()

            print('Image Successfully saved ...')
            return HttpResponse("Text only, please.", content_type="text/plain")
        except:
            pass
