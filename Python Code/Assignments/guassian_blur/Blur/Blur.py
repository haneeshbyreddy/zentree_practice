from PIL import Image
import numpy as np

class Gaussian_blur:

    def __init__(self):
        self.gf = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]
        self.sigma = -1

    def set_gf(self, gf):
        self.gf = gf

    def add_padding(self, matrix, m, n):
        return np.pad(matrix, [(m,), (n,), (0,)], mode='constant')

    def image_gen(self, image_gf, to_path):
        image_gf.save(to_path)

    def apply_filter(self, image_matrix, gf, channel=1):
        h1, w1 = len(image_matrix), len(image_matrix[0])
        h2, w2 = len(gf), len(gf[0])
        image_matrix = self.add_padding(image_matrix, h2//2, w2//2)
        new_image_matrix = np.zeros((h1, w1, channel), dtype=np.uint8)
        for d in range(channel):
            for i in range(h1-h2+1):
                for j in range(w1-w2+1):
                    temp = 0
                    for m in range(h2):
                        for n in range(w2):
                            temp += (int(image_matrix[i+m][j+n][d]) * gf[m][n])
                    new_image_matrix[i][j][d] = temp
        if channel==1:
            image_gf = Image.fromarray(new_image_matrix.reshape((h1,w1)))
            image_gf = image_gf.convert('L')
        else:
            image_gf = Image.fromarray(new_image_matrix, mode="RGB")
            image_gf = image_gf.convert('RGB')
        return image_gf


    def gaussian_kernal(self, size, sigma=-1):
        sigma = self.sigma if sigma==-1 else sigma
        func = lambda x, y : (1/(2*np.pi*sigma**2)) * np.exp(-((x-(size-1)/2)**2 + (y-(size-1)/2)**2) / (2*sigma**2))
        kernal = np.zeros((size, size))
        for i in range(size):
            for j in range(size):
                kernal[i][j] = func(i, j)
        kernal /= np.sum(kernal)
        return kernal

    def blur(self, path, sigma=-1, color=False):
        kernel_size = 2 * int(np.ceil(3 * sigma)) + 1
        if sigma>0 and self.sigma != sigma:
            self.sigma = sigma
            self.gf = self.gaussian_kernal(kernel_size)
        with Image.open(path) as input_image:
            image = input_image.convert('RGB') if color else input_image.convert("L")
            image_matrix = np.array(image)
            return self.apply_filter(image_matrix, self.gf, channel=3 if color else 0)