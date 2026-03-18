import cv2

image = cv2.imread("iron_man.jpg")

blurred_image = cv2.GaussianBlur(image, (20, 20), 0)

cv2.imwrite("blurred_output.jpg", blurred_image)

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()