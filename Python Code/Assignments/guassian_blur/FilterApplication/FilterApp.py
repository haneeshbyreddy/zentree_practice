from PIL import Image
from Blur.Blur import Gaussian_blur
import matplotlib.pyplot as plt
import math
import os

class FilterApp:

    def __init__(self):
        self.gb = Gaussian_blur()
        self.images = []
        self.names = []

    def matrix_to_image(self,image_matrix):
        shape = image_matrix.shape
        if len(shape) == 2:
            image = Image.fromarray(image_matrix)
            image = image.convert('L')
        if len(shape) == 3:
            image = Image.fromarray(image_matrix, mode="RGB")
            image = image.convert('RGB')
        return image

    # def add_images(self, file_name, input_location, output_location, color):
    #     out_path = output_location + file_name + ("-color-" if color else "-") + self.image_name
    #     if not os.path.exists(out_path):
    #         with Image.open(input_location+self.image_name) as input_image:
    #             image = input_image.convert('RGB') if color else input_image.convert("L")
    #             self.matrix_to_image(self.gb.blur(image, i, color=color)).save(out_path)
    #     self.images.append(plt.imread(out_path))
    #     self.names.append(f"Image with sigma value {i}")


    def add_sigma_images(self,sigmas,input_location,output_location,color):
            for i in sigmas:
                out_path = output_location + '-'.join([str(i),"sigma","color" if color else "",self.image_name])
                if not os.path.exists(out_path):
                    with Image.open(input_location+self.image_name) as input_image:
                        image = input_image.convert('RGB') if color else input_image.convert("L")
                        self.matrix_to_image(self.gb.blur(image, i, color=color)).save(out_path)
                self.images.append(plt.imread(out_path))
                self.names.append(f"Image with sigma value {i}")

    def add_edge_images(self,input_location,output_location,color):
            paths = ["vertical_edge", "horizontal_edge", "vertical_and_horizontal"]
            for i,edge_name in enumerate(paths):
                out_path = output_location + edge_name + ("-color-" if color else "-") + self.image_name
                if not os.path.exists(out_path):
                    with Image.open(input_location+self.image_name) as input_image:
                        image = input_image.convert('RGB') if color else input_image.convert("L")
                        self.matrix_to_image(self.gb.edge(image, edge=i, color=color)).save(out_path)
                self.images.append(plt.imread(out_path))
                self.names.append(f"{edge_name} Filter")
        
    def add_laplacian(self,input_location,output_location,color):
            out_path = output_location + "laplacian" + ("-color-" if color else "-") + self.image_name
            if not os.path.exists(out_path):
                with Image.open(input_location+self.image_name) as input_image:
                    image = input_image.convert('RGB') if color else input_image.convert("L")
                    self.matrix_to_image(self.gb.laplacian(image,color=color)).save(out_path)
            self.images.append(plt.imread(out_path))
            self.names.append("Laplacian Filter")


    def start(self,image_name,input_location,output_location,sigmas=[],edge=False,color=True,laplacian=False):
        self.image_name = image_name
        self.images.append(plt.imread(input_location+self.image_name))
        self.names.append("Original image")

        if len(sigmas)>0:
            self.add_sigma_images(sigmas,input_location,output_location,color=color)
        if edge:
            self.add_edge_images(input_location,output_location,color=color)
        if laplacian:
            self.add_laplacian(input_location,output_location,color=color)
        
    def plot(self):
        n = len(self.images)
        w = math.ceil(math.sqrt(n))

        plt.figure(figsize=(25,25))

        for i in range(len(self.images)):
            plt.subplot(math.ceil(n/w),w,i+1)
            plt.imshow(self.images[i],cmap='gray')
            plt.title(self.names[i])
        plt.show()