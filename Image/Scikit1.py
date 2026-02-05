from skimage import io, color
import matplotlib.pyplot as plt

original_image = io.imread('iron_man.jpg')

height, width, channels = original_image.shape
print(f"Image loaded with height: {height}, width: {width}, and channels: {channels}")

gray_image = color.rgb2gray(original_image)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")

plt.tight_layout()
plt.show()
