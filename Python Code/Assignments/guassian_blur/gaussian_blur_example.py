from Blur import Gaussian_blur
import matplotlib.pyplot as plt
import math
import os
import time

gb = Gaussian_blur()

image_files = os.listdir("data/input")
for i, image_file in enumerate(image_files):
    print(f"{i} : {image_file}")
index = int(input("Enter a index of image :"))
image_name = image_files[index]
color = bool(True if input("Do you want color [y/n]:") =='y' else False)

start_time = time.time()

sigmas = [round(i*0.1,1) for i in range(5,50,5)]
n = len(sigmas)+1
w = math.ceil(math.sqrt(n))
blurred_images = []

for i in sigmas:
    out_path = "data/output/" + '-'.join([str(i),image_name])
    if not os.path.exists(out_path):
        blur_image = gb.blur("data/input/"+image_name, i, color=color)
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

end_time = time.time()
print("time taken", end_time - start_time)

plt.show()