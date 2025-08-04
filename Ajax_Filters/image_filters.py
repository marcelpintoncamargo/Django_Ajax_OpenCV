import cv2
import numpy as np
import scipy.ndimage as nd


def first_order_filter_function(image, filter_name, kernel_first_order, lim_inf_canny, lim_sup_canny, kernel_canny):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    if filter_name == 'Sobel X':
        sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=kernel_first_order)
        sobel_x = np.absolute(sobel_x)
        sobel_x = np.uint8(sobel_x)
        output_image = sobel_x

    elif filter_name == 'Sobel Y':
        sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=kernel_first_order)
        sobel_y = np.absolute(sobel_y)
        sobel_y = np.uint8(sobel_y)
        output_image = sobel_y

    elif filter_name == 'Sobel X+Y':
        sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=kernel_first_order)
        sobel_x = np.absolute(sobel_x)
        sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=kernel_first_order)
        sobel_y = np.absolute(sobel_y)
        sobel_x_y = sobel_x + sobel_y
        sobel_x_y = np.uint8(sobel_x_y)
        output_image = sobel_x_y

    elif filter_name == 'Scharr X':
        scharr_x = cv2.Scharr(gray, cv2.CV_64F, 1, 0)
        # scharr_x = cv2.convertScaleAbs(scharr_x)
        scharr_x = np.absolute(scharr_x)
        scharr_x = np.uint8(scharr_x)
        output_image = scharr_x

    elif filter_name == 'Scharr Y':
        scharr_y = cv2.Scharr(gray, cv2.CV_64F, 0, 1)
        # scharr_y = cv2.convertScaleAbs(scharr_y)
        scharr_y = np.absolute(scharr_y)
        scharr_y = np.uint8(scharr_y)
        output_image = scharr_y

    elif filter_name == 'Canny':
        canny = cv2.Canny(gray, lim_inf_canny, lim_sup_canny, apertureSize=kernel_canny, L2gradient=True)
        output_image = canny

    output_image_1D = np.ravel(output_image)
    output_image_list = output_image_1D.tolist()
    channel_01 = output_image_list
    channel_02 = output_image_list
    channel_03 = output_image_list
    print('Image Processed !!!')
    return channel_01, channel_02, channel_03


# noinspection PyGlobalUndefined
def second_order_filter_function(image, filter_name, kernel_second_order, sigma_laplace_of_gaussian, sharp_laplacian_w1,
                                 sharp_laplacian_w2, sharp_laplacian_alpha):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    if filter_name == 'Laplacian':
        laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=kernel_second_order)
        laplacian = np.absolute(laplacian)
        laplacian = np.uint8(laplacian)
        output_image = laplacian

    elif filter_name == 'Laplacian of Gaussian':
        laplacian_of_gaussian = nd.gaussian_laplace(gray, sigma=sigma_laplace_of_gaussian)
        laplacian_of_gaussian = np.absolute(laplacian_of_gaussian)
        laplacian_of_gaussian = np.uint8(laplacian_of_gaussian)
        output_image = laplacian_of_gaussian

    elif filter_name == 'Sharpenning Laplacian':
        laplace = cv2.Laplacian(gray, cv2.CV_64F, ksize=kernel_second_order)
        laplace = np.absolute(laplace)
        laplace = np.uint8(laplace)
        sharpenning_laplacian = cv2.addWeighted(laplace, sharp_laplacian_w1, gray, sharp_laplacian_w2,
                                                sharp_laplacian_alpha)
        output_image = sharpenning_laplacian

    elif filter_name == 'Sharpenning Laplacian of Gaussian':
        laplacian_of_gaussian = nd.gaussian_laplace(gray, sigma=sigma_laplace_of_gaussian)
        laplacian_of_gaussian = np.absolute(laplacian_of_gaussian)
        laplacian_of_gaussian = np.uint8(laplacian_of_gaussian)
        sharpenning_laplacian_of_gaussian = cv2.addWeighted(laplacian_of_gaussian, sharp_laplacian_w1, gray,
                                                            sharp_laplacian_w2, sharp_laplacian_alpha)
        output_image = sharpenning_laplacian_of_gaussian

    output_image_1D = np.ravel(output_image)
    output_image_list = output_image_1D.tolist()
    channel_01 = output_image_list
    channel_02 = output_image_list
    channel_03 = output_image_list
    print('Image Processed !!!')
    return channel_01, channel_02, channel_03



def blur_filter_function(image, filter_name, kernel_blur, sigma_x_blur, sigma_y_blur, mean_filter_option):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    if filter_name == 'Gaussian Blur':
        gaussian_blur = cv2.GaussianBlur(gray, (kernel_blur, kernel_blur), sigma_x_blur, sigma_y_blur)
        output_image = gaussian_blur

    elif filter_name == 'Median Filter':
        median_filter = cv2.medianBlur(gray, (kernel_blur))
        output_image = median_filter

    elif filter_name == 'Bilateral Filter':
        bilateral_filter = cv2.bilateralFilter(gray, kernel_blur, 75, 75)
        output_image = bilateral_filter

    elif filter_name == 'Mean Filter' and mean_filter_option == 'True':
        mean_filter = cv2.boxFilter(gray, 0, (kernel_blur, kernel_blur), 0, (-1, -1), True, cv2.BORDER_DEFAULT)
        output_image = mean_filter

    elif filter_name == 'Mean Filter' and mean_filter_option == 'False':
        mean_filter = cv2.boxFilter(gray, 0, (kernel_blur, kernel_blur), 0, (-1, -1), False, cv2.BORDER_DEFAULT)
        output_image = mean_filter

    output_image_1D = np.ravel(output_image)
    output_image_list = output_image_1D.tolist()
    channel_01 = output_image_list
    channel_02 = output_image_list
    channel_03 = output_image_list
    print('Image Processed !!!')
    return channel_01, channel_02, channel_03


def threshold_filter_function(image, threshold_name, threshold_value, threshold_max_value):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    if threshold_name == 'cv2.THRESH_TOZERO':
        ret, thresh_image = cv2.threshold(gray, threshold_value, threshold_max_value, cv2.THRESH_TOZERO)
        output_image = thresh_image

    elif threshold_name == 'cv2.THRESH_TOZERO_INV':
        ret, thresh_image = cv2.threshold(gray, threshold_value, threshold_max_value, cv2.THRESH_TOZERO_INV)
        output_image = thresh_image

    elif threshold_name == 'cv2.THRESH_BINARY':
        ret, thresh_image = cv2.threshold(gray, threshold_value, threshold_max_value, cv2.THRESH_BINARY)
        output_image = thresh_image

    elif threshold_name == 'cv2.THRESH_BINARY_INV':
        ret, thresh_image = cv2.threshold(gray, threshold_value, threshold_max_value, cv2.THRESH_BINARY_INV)
        output_image = thresh_image

    elif threshold_name == 'cv2.THRESH_TRUNC':
        ret, thresh_image = cv2.threshold(gray, threshold_value, threshold_max_value, cv2.THRESH_TRUNC)
        output_image = thresh_image

    elif threshold_name == 'cv2.THRESH_OTSU':
        ret, thresh_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        output_image = thresh_image

    output_image_1D = np.ravel(output_image)
    output_image_list = output_image_1D.tolist()
    channel_01 = output_image_list
    channel_02 = output_image_list
    channel_03 = output_image_list
    print('Image Processed !!!')
    return channel_01, channel_02, channel_03

def space_transformation_function(image, filter_name):

    if filter_name == 'Original':
        output_image = image

    elif filter_name == 'RGB2HSV':
        output_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    elif filter_name == 'RGB2GRAY':
        output_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    elif filter_name == 'Red Channel':
        output_image = image[:,:,0]

    elif filter_name == 'Hue Channel':
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        hue = hsv[:, :, 0]
        output_image = hue

    print('image length: ', len(np.shape(output_image)))

    if len(np.shape(output_image)) > 2:  #!** image length = 3 (rows, columns, channels)

        first_channel = output_image[:,:,0]
        second_channel = output_image[:,:,1]
        third_channel = output_image[:,:,2]

        first_channel_1D = np.ravel(first_channel)
        second_channel_1D = np.ravel(second_channel)
        third_channel_1D = np.ravel(third_channel)

        first_channel_1D_list = first_channel_1D.tolist()
        second_channel_1D_list = second_channel_1D.tolist()
        third_channel_1D_list = third_channel_1D.tolist()

        channel_01 = first_channel_1D_list
        channel_02 = second_channel_1D_list
        channel_03 = third_channel_1D_list
        print('Image Processed !!!')
        return channel_01, channel_02, channel_03

    else:             # *** image length = 2 (rows, columns)
        output_image_1D = np.ravel(output_image)
        output_image_list = output_image_1D.tolist()
        channel_01 = output_image_list
        channel_02 = output_image_list
        channel_03 = output_image_list
        print('Image Processed !!!')
        return channel_01, channel_02, channel_03




