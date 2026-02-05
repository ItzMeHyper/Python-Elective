from PIL import Image

img = Image.open("iron_man.jpg")
gray_image = img.convert('L')

img.show(title="Original Image")
gray_image.show(title="Grayscale Image")
gray_image.save('output_gray.jpg')