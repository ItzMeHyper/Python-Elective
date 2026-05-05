import cv2

img = cv2.imread("iron_man.jpg")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', gray_image)

#Resize
resized = cv2.resize(img, (300, 300))
cv2.imshow('Resized Image', resized)

#Rotate
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated Image', rotated)

#cropped
crop = img[50:200, 50:200]
cv2.imshow('Cropped Image', crop)

#Blur
blur = cv2.GaussianBlur(img, (21,21), 0)
cv2.imshow('Blurred Image', blur)

#Edge Detection
edges = cv2.Canny(img, 100, 200)
cv2.imshow('Edge Detected Image', edges)

cv2.waitKey(0)

cv2.destroyAllWindows()

