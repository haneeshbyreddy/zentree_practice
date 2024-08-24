from Blur.Blur import Gaussian_blur
import matplotlib.pyplot as plt
import math
import os

class FilterApp:

    def __init__(self):
        self.gb = Gaussian_blur()
        self.sigmas = []
        self.images = []
        self.names = []

    def add_sigma_images(self,sigmas,input_location,output_location):
            for i in sigmas:
                out_path = output_location + '-'.join([str(i),"sigma",self.image_name])
                if not os.path.exists(out_path):
                    blur_image = self.gb.blur(input_location+self.image_name, i, color=True)
                    blur_image.save(out_path)
                self.images.append(plt.imread(out_path))
                self.names.append(f"Image with sigma value {i}")

    def add_edge_images(self,input_location,output_location):
            out_path = output_location+"vertical-edge-" + self.image_name
            if not os.path.exists(out_path):
                blur_image = self.gb.edge(input_location+self.image_name, edge=0)
                blur_image.save(out_path)
            self.images.append(plt.imread(out_path))
            self.names.append("Vertical Edge Filter")

            out_path = output_location+"horizontal-edge-" + self.image_name
            if not os.path.exists(out_path):
                blur_image = self.gb.edge(input_location+self.image_name, edge=1)
                blur_image.save(out_path)
            self.images.append(plt.imread(out_path))
            self.names.append("Horizontal Edge Filter")

    def start(self,input_location,output_location,sigmas=[],edge=False):

        image_files = os.listdir(input_location)
        for i, image_file in enumerate(image_files):
            print(f"{i} : {image_file}")
        index = int(input("Enter a index of image :"))
        self.image_name = image_files[index]

        self.images.append(plt.imread(input_location+self.image_name))
        self.names.append("Original image")

        if len(sigmas)>0:
            self.add_sigma_images(sigmas,input_location,output_location)
        if edge:
            self.add_edge_images(input_location,output_location)
        
    def plot(self):

        n = len(self.images)
        w = math.ceil(math.sqrt(n))

        plt.figure(figsize=(25,25))

        for i in range(len(self.images)):
            plt.subplot(math.ceil(n/w),w,i+1)
            plt.imshow(self.images[i])
            plt.title(self.names[i])
        plt.show()