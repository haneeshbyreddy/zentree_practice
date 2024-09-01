from Layers import Layers
from PIL import Image
import numpy as np
import time
import idx2numpy

file_path_img = 'data/input/train-images-idx3-ubyte'
file_path_label = 'data/input/train-labels-idx1-ubyte'

images = idx2numpy.convert_from_file(file_path_img)
labels = idx2numpy.convert_from_file(file_path_label)

img = images[0]
true_output = [0 if labels[0] != i else 1 for i in range(10)]

lay = Layers()

start_time = time.time()

stacks = [16, 32, 64]
for i in stacks:
    stack = lay.conv(np.array(img), i)
    stack_maxpool = lay.maxpool(stack)
    stack_relu = lay.relu(stack_maxpool)
    print(stack_relu.shape)
    img = stack_relu

output = lay.flatten(img)
print("flattened :", output)

fc_layers = [128, 64]
for i in fc_layers:
    fc_out = lay.fc(output, i)
    fc_relu = lay.relu(fc_out)
    output = fc_relu
    print("fc output :", output.shape)

final = lay.fc(output, 10)
final = lay.softmax(final)
print("softmax values :", final)

loss = lay.loss_function(final, true_output)
print("loss :", loss)

end_time = time.time()
print("\nTime taken :", end_time-start_time)