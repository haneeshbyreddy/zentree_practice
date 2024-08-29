from PIL import Image, ImageFilter
from Blur.Blur import Gaussian_blur
import numpy as np
import cv2
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

    def add_sigma_images(self,sigmas):
        for i in sigmas:
            out_path = self.output_location + '-'.join([str(i),"sigma","color" if self.color else "",self.image_name])
            if not os.path.exists(out_path):
                with Image.open(self.input_location+self.image_name) as input_image:
                    image = input_image.convert('RGB') if self.color else input_image.convert("L")
                    self.matrix_to_image(self.gb.blur(image, i, color=self.color)).save(out_path)
            self.images.append(plt.imread(out_path))
            self.names.append(f"Image with sigma value {i}")

    def add_edge_images(self):
        paths = ["vertical_edge", "horizontal_edge"]
        for i,edge_name in enumerate(paths):
            out_path = self.output_location + edge_name + ("-color-" if self.color else "-") + self.image_name
            if not os.path.exists(out_path):
                with Image.open(self.input_location+self.image_name) as input_image:
                    image = input_image.convert('RGB') if self.color else input_image.convert("L")
                    self.matrix_to_image(self.gb.edge(image, edge=i, color=self.color)).save(out_path)
            self.images.append(plt.imread(out_path))
            self.names.append(f"{edge_name} Filter")
        
    def add_laplacian(self):
        out_path = self.output_location + "laplacian" + ("-color-" if self.color else "-") + self.image_name
        if not os.path.exists(out_path):
            with Image.open(self.input_location+self.image_name) as input_image:
                image = input_image.convert('RGB') if self.color else input_image.convert("L")
                self.matrix_to_image(self.gb.laplacian(image,color=self.color)).save(out_path)
        self.images.append(plt.imread(out_path))
        self.names.append("Laplacian Filter")
    
    def edge_detection(self):
        out_path = self.output_location + "canny" + ("-color-" if self.color else "-") + self.image_name
        if not os.path.exists(out_path):
            with Image.open(self.input_location + self.image_name) as input_image:
                image = np.array(input_image.convert('RGB') if self.color else input_image.convert("L"))
                edges = self.gb.canny(image,self.color)
                edge_image = self.matrix_to_image(edges)
                edge_image.save(out_path)
        self.images.append(plt.imread(out_path))
        self.names.append("Canny Edge Detection")

    def edge_detection_1(self):
        out_path = self.output_location + "canny_default" + ("-color-" if self.color else "-") + self.image_name
        if not os.path.exists(out_path):
            with Image.open(self.input_location + self.image_name) as input_image:
                image = np.array(input_image.convert('RGB') if self.color else input_image.convert("L"))
                edges = cv2.Canny(image, threshold1=100, threshold2=200)
                edge_image = self.matrix_to_image(edges)
                edge_image.save(out_path)
        self.images.append(plt.imread(out_path))
        self.names.append("CV2 Canny Edge Detection")


    def start(self,image_name,input_location,output_location,sigmas=[],edge=False,color=True):
        self.image_name = image_name
        self.input_location = input_location
        self.output_location = output_location
        self.color = color
        self.images.append(plt.imread(input_location+self.image_name))
        self.names.append("Original image")

        if len(sigmas)>0:
            self.add_sigma_images(sigmas)
        if edge:
            self.add_edge_images()
            self.add_laplacian()
            self.edge_detection()
            self.edge_detection_1()
        
    def plot(self):
        n = len(self.images)
        w = math.ceil(math.sqrt(n))

        plt.figure(figsize=(25,25))

        for i in range(len(self.images)):
            plt.subplot(math.ceil(n/w),w,i+1)
            plt.imshow(self.images[i],cmap='gray')
            plt.axis('off')
            plt.title(self.names[i])
        plt.show()