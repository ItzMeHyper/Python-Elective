from PIL import Image

img = Image.open("iron_man.jpg")

bw = img.convert("L")

img.show()
bw.save("bw_image.jpg")
bw.show()