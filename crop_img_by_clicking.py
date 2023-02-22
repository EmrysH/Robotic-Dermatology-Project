import cv2
import numpy as np

clicked_pixels = []

img = []
img_original = []
img_cropped = []

FLAG_cropping_finished = False

def crop_image(image_full_path, show_resulting_image = False):
    global img
    global img_original
    global img_cropped
    global FLAG_cropping_finished

    img = cv2.imread(image_full_path, 1)
    img_original = cv2.imread(image_full_path, 1)
    cv2.imshow('image_to_crop', img)
    cv2.setMouseCallback('image_to_crop', click_event)
    while(FLAG_cropping_finished == False):
        k = cv2.waitKey(1)
    if (show_resulting_image):
        cv2.imshow('img_cropped', img_cropped)
        cv2.waitKey(0)
        cv2.cv2.destroyWindow("img_cropped")
    return img_cropped


def click_event(event, x, y, flags, params):
    global img
    global img_original
    global img_cropped
    global FLAG_cropping_finished

    # Create crop selection-pivots by left clicking on the image
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_pixels.append((x, y))
        for index, line in enumerate(clicked_pixels):
            cv2.circle(img, line, 6, (0, 0, 255), 4)
            if (len(clicked_pixels) == index+1):
                break
            cv2.line(img, clicked_pixels[index], clicked_pixels[index + 1], (0, 255, 0), 2)
        cv2.imshow('image_to_crop', img)

    # Close selection with right click and crop image
    if event == cv2.EVENT_RBUTTONDOWN:
        clicked_pixels.append(clicked_pixels[0])
        height = img.shape[0]
        width = img.shape[1]
        mask = np.zeros((height, width), dtype=np.uint8)
        points = np.array([clicked_pixels])

        cv2.fillPoly(mask, points, (255))
        res = cv2.bitwise_and(img_original, img_original, mask=mask)
        rect = cv2.boundingRect(points)
        img_cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
        cv2.destroyWindow("image_to_crop")
        FLAG_cropping_finished = True