from Layers import Layers
from PIL import Image
import numpy as np
import idx2numpy

file_path_img = 'data/input/train-images-idx3-ubyte'
file_path_label = 'data/input/train-labels-idx1-ubyte'

images = idx2numpy.convert_from_file(file_path_img)
labels = idx2numpy.convert_from_file(file_path_label)

img = images[0]
true_output = [0 if labels[0] != i else 1 for i in range(10)]
stacks = [16, 32, 64]
fc_weights = [23104, 128, 64, 10]

lay = Layers()

weights = lay.backtrack(images[:10], labels[:10], stacks, fc_weights)

img = lay.apply_stacks(img, stacks)

flattened = lay.flatten(img)

output = lay.apply_fc(flattened, weights)

print("Before softmax values :", np.round(output,1))

final = lay.softmax(output)

print("softmax values :", np.round(final,1))