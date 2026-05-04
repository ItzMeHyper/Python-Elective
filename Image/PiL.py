from PIL import Image

img = Image.open("iron_man.jpg")
img.show(title="Original Image")

gray_image = img.convert('L')
gray_image.show(title="Grayscale Image")
gray_image.save('output_gray.jpg')

#Resize
resized = img.resize((200, 200))
resized.show()

#Rotate
rotated = img.rotate(90)
rotated.show()

#Crop
cropped = img.crop((50, 50, 200, 200))
cropped.show()