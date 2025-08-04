import cv2

def get_filtered_image(image, action):

    if action == 'NO_FILTER':
        filtered = image

    elif action == 'HSV':
        filtered = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    elif action == 'GRAYSCALE':
        filtered = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    elif action == 'BLURRED':
        width, height = image.shape[:2]
        if width > 500:
            k = (50,50)
        elif width > 200 and width <= 500:
            k = (25,25)
        else:
            k = (10, 10)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        filtered = cv2.blur(gray, k)
        #filtered = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)

    elif action == 'BINARY':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, filtered = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    elif action == 'INVERT':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret , bw = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        filtered = cv2.bitwise_not(bw)

    return filtered

