from Blur import Gaussian_blur
import matplotlib.pyplot as plt

gb = Gaussian_blur()

original_image = plt.imread('data/input-2.png')
image_gf_1 = gb.blur('data/input-2.png', 0.5)
image_gf_2 = gb.blur('data/input-2.png', 1)
image_gf_3 = gb.blur('data/input-2.png', 1.5)

plt.figure(figsize=(25,25))
plt.subplot(2,2,1)
plt.imshow(original_image, cmap='gray')
plt.subplot(2,2,2)
plt.imshow(image_gf_1, cmap='gray')
plt.subplot(2,2,3)
plt.imshow(image_gf_2, cmap='gray')
plt.subplot(2,2,4)
plt.imshow(image_gf_3, cmap='gray')
plt.show()