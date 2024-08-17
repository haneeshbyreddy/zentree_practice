from PIL import Image
import numpy as np

def apply_filter(image, fil):
    h1, w1 = len(image), len(image[0])
    h2, w2 = len(fil), len(fil[0])
    new_image = np.zeros((h1-h2+1, w1-w2+1))
    print('flag')
    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            temp = 0
            for m in range(h2):
                for n in range(w2):
                    temp += (int(image[i+m][j+n]) * fil[m][n])
            new_image[i][j] = temp
    return new_image

image = Image.open('grayscale.jpg')
image = image.convert('L')
image_matrix = np.array(image)
print(image_matrix.shape)

gf = [[1,0,-1],[1,0,-1],[1,0,-1]]
image_matrix_fil = apply_filter(image_matrix, gf)
print(image_matrix_fil.shape)

image_fil = Image.fromarray(image_matrix_fil)
image_fil = image_fil.convert('L')
image_fil.save("output.jpg")