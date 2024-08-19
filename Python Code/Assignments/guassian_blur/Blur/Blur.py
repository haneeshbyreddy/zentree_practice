from PIL import Image
import numpy as np

class Gaussian_blur:

    def __init__(self):
        self.gf = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]

    def gaussian_kernal(size, sigma):
        func = lambda x, y : (1/(2*np.pi*sigma**2)) * np.exp(-((x-(size-1)/2)**2 + (y-(size-1)/2)**2) / (2*sigma**2))
        kernal = np.zeros((size, size))
        for i in range(size):
            for j in range(size):
                kernal[i][j] = func(i, j)
        kernal /= np.sum(kernal)
        return kernal
    
    def image_gen(self, image_matrix):
        image_gf = Image.fromarray(image_matrix)
        image_gf = image_gf.convert('L')
        image_gf.save(self.to_path)

    def apply_filter(self, image_matrix, gf):
        h1, w1 = len(image_matrix), len(image_matrix[0])
        h2, w2 = len(gf), len(gf[0])
        new_image_matrix = np.zeros((h1-h2+1, w1-w2+1))
        for i in range(h1-h2+1):
            for j in range(w1-w2+1):
                temp = 0
                for m in range(h2):
                    for n in range(w2):
                        temp += (int(image_matrix[i+m][j+n]) * gf[m][n])
                new_image_matrix[i][j] = temp
        self.image_gen(new_image_matrix)

    def blur(self, path, to_path, sigma):
        self.to_path = to_path
        with Image.open(path) as image:
            image_gray = image.convert('L')
            image_matrix = np.array(image_gray)
            self.apply_filter(image_matrix, self.gf)
        
    def set_gf(self, gf):
        self.gf = gf