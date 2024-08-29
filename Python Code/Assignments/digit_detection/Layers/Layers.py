import numpy as np
import random

class Layers:
    def __init__(self):
        pass
    
    def apply_filter(self, image_matrix, gf):
        h1, w1 = image_matrix.shape[:2]
        h2, w2 = gf.shape[:2]
        if len(image_matrix.shape)>2:
            image_matrix = np.pad(image_matrix, ((h2,),(w2,),(0,)), mode='constant')
        else:
            image_matrix = np.stack([np.pad(image_matrix, ((h2,),(w2,)), mode='constant')],-1)

        d = image_matrix.shape[2]

        new_image_matrix = np.zeros((h1, w1), dtype=np.uint8)
        for d in range(d):
            for i in range(h1):
                for j in range(w1):
                    temp = np.sum(image_matrix[i:i+h2, j:j+w2, d] * gf)
                    new_image_matrix[i, j] += temp

        return new_image_matrix

    def gaussian_kernal(self, size, sigma=-1):
        func = lambda x, y : (1/(2*np.pi*sigma**2)) * np.exp(-((x-(size-1)/2)**2 + (y-(size-1)/2)**2) / (2*sigma**2))
        kernal = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                kernal[i][j] = func(i, j)
        kernal /= np.sum(kernal)
        return kernal

    def blur(self, image_matrix, n):
        arr = []
        random.seed(10)
        for _ in range(n):
            rand = round(random.random()+0.1, 1)
            gf = self.gaussian_kernal(2*int(np.ceil(3*rand))+1, rand)
            arr.append(self.apply_filter(image_matrix, gf))
        return np.stack(arr, -1)

    def maxpool(self, image_matrix, maxpoll=2):
        h1, w1 = image_matrix.shape[:2]

        if len(image_matrix.shape)>2:
            image_matrix = np.pad(image_matrix, ((maxpoll,),(maxpoll,),(0,)), mode='constant')
        else:
            image_matrix = np.stack([np.pad(image_matrix, ((maxpoll,),(maxpoll,)), mode='constant')],-1)

        d = image_matrix.shape[2]
        new_image_matrix = np.zeros((h1, w1,d), dtype=np.uint8)
        for d in range(d):
            for i in range(h1):
                for j in range(w1):
                    temp = np.max(image_matrix[i:i+maxpoll, j:j+maxpoll, d])
                    new_image_matrix[i, j, d] = temp
        return new_image_matrix
    
    def relu(self, image_matrix):
        return np.maximum(0, image_matrix)
    
    def flatten(self, image_matrix):
        return image_matrix.ravel()