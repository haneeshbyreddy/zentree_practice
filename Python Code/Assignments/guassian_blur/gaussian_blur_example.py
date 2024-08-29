from FilterApplication import FilterApp
import time
import os

fl = FilterApp()

start_time = time.time()

input_images, output_images = "data/input/", "data/output/"

image_files = os.listdir(input_images)
for i, image_file in enumerate(image_files):
    print(f"{i} : {image_file}")
index = int(input("Enter a index of image :"))
image_name = image_files[index]
print(image_name)

color = bool(input("Do you want color images [y/n]:")=='y')
gaussian = bool(input("Do you want gaussian images [y/n]:")=='y')
edge = bool(input("Do you want edge images [y/n]:")=='y')
sigmas = [1,2]

fl.start(image_name,input_images,output_images,sigmas=sigmas if gaussian else [],edge=edge,color=color)
end_time = time.time()
fl.plot()
print("Total Time Taken :",end_time-start_time)