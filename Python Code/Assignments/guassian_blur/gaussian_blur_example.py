from Blur import Gaussian_blur
import matplotlib.pyplot as plt
import math
import os

gb = Gaussian_blur()

image_name = 'input-3.png'

sigmas, color = [round(i*0.1,1) for i in range(1,10,2)], True
n = len(sigmas)+1
w = math.ceil(math.sqrt(n))
blurred_images = []

for i in sigmas:
    out_path = "data/output/" + '-'.join([str(i),image_name])
    if not os.path.exists(out_path):
        blur_image = gb.blur("data/input/"+image_name, i, color=True)
        blur_image.save(out_path)
    blurred_images.append(plt.imread(out_path))

plt.figure(figsize=(25,25))

plt.subplot(math.ceil(n/w),w,1)
plt.imshow(plt.imread("data/input/"+image_name))
plt.title(f"Original Image")

for i in range(len(blurred_images)):
    plt.subplot(math.ceil(n/w),w,i+2)
    plt.imshow(blurred_images[i])
    plt.title(f"image with sigma : {sigmas[i]}")

plt.show()