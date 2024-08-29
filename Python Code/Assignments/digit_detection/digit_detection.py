from Layers import Layers
from PIL import Image
import numpy as np
import time

'''
Covolve(3,16)
Maxpool(2,2)
Relu
Covolve(16,32)
Maxpool(2,2)
Relu
Covolve(32,64)
Maxpool(2,2)
Relu

Flatten(128)

Fully Connected(128)
Relu
Fully Connected(128,64)
Relu
Fully Connected(64,10)

Output
'''

lay = Layers()
with Image.open('data/input/1.jpeg') as img:
    img = img.convert('L')

    start_time = time.time()

    stack_1 = lay.blur(np.array(img), 16)
    stack_1_maxpool = lay.maxpool(stack_1)
    stack_1_relu = lay.relu(stack_1_maxpool)

    stack_2 = lay.blur(np.array(stack_1_relu), 32)
    stack_2_maxpool = lay.maxpool(stack_2)
    stack_2_relu = lay.relu(stack_2_maxpool)

    stack_3 = lay.blur(np.array(stack_2_relu), 64)
    stack_3_maxpool = lay.maxpool(stack_3)
    stack_3_relu = lay.relu(stack_3_maxpool)

    end_time = time.time()

    print("Time taken :", end_time-start_time)
    print(stack_3_relu.shape)
    print(lay.flatten(stack_3_relu))