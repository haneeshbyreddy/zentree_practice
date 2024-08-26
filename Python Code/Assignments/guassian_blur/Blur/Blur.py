import numpy as np

class Gaussian_blur:

    def add_padding(self, matrix, *args):
        arr = []
        for i in args:
            arr.append((i,))
        return np.pad(matrix, arr, mode='constant')

    def apply_filter(self, image_matrix, gf, channel=3):
        h1, w1 = image_matrix.shape[0], image_matrix.shape[1]
        h2, w2 = gf.shape[0], gf.shape[1]
        if channel==3:
            image_matrix = self.add_padding(image_matrix, h2//2, w2//2,0)
        else:
            image_matrix = np.stack([self.add_padding(image_matrix, h2//2, w2//2)],-1)

        new_image_matrix = np.zeros((h1, w1, channel), dtype=np.uint8)
        for d in range(channel):
            for i in range(h1):
                for j in range(w1):
                    temp = np.sum(image_matrix[i:i+h2, j:j+w2, d] * gf[:,:,d])
                    new_image_matrix[i, j, d] = temp
        if channel == 1:
            new_image_matrix = new_image_matrix[:,:,0]
        return new_image_matrix

    def gaussian_kernal(self, size, sigma=-1):
        func = lambda x, y : (1/(2*np.pi*sigma**2)) * np.exp(-((x-(size-1)/2)**2 + (y-(size-1)/2)**2) / (2*sigma**2))
        kernal = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                kernal[i][j] = func(i, j)
        kernal /= np.sum(kernal)
        return kernal

    def blur(self, image, sigma=-1, color=False):
        gf = self.gaussian_kernal(2*int(np.ceil(3*sigma))+1)
        return self.apply_filter(np.array(image), np.stack([gf]*3,-1), channel=3 if color else 1)

    def edge(self, image, edge, color):
        image_matrix = np.array(image)
        if edge==0:
            fil = [[1,0,-1],[1,0,-1],[1,0,-1]]
            return self.apply_filter(image_matrix, np.stack([fil]*3,-1), channel=3 if color else 1)
        elif edge==1: 
            fil = [[1,1,1],[0,0,0],[-1,-1,-1]]
            return self.apply_filter(image_matrix, np.stack([fil]*3,-1), channel=3 if color else 1)
        else:
            fil = [[1,0,-1],[1,0,-1],[1,0,-1]]
            matrix = self.apply_filter(image_matrix, np.stack([fil]*3,-1), channel=3 if color else 1) 
            fil = [[1,1,1],[0,0,0],[-1,-1,-1]]
            return self.apply_filter(matrix, np.stack([fil]*3,-1), channel=3 if color else 1)