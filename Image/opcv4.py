import cv2

def shrink_image(image, factor):
    height, width = image.shape[:2]

    new_width = width // factor
    new_height = height // factor

    shrunk_image = cv2.resize(image, (new_width, new_height))
    return shrunk_image

img = cv2.imread("iron_man.jpg")

small_img = shrink_image(img, 2)