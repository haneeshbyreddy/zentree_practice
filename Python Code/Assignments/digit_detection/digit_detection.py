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

    stack_1 = lay.conv(np.array(img), 16)
    stack_1_maxpool = lay.maxpool(stack_1)
    stack_1_relu = lay.relu(stack_1_maxpool)
    print(stack_1_relu.shape)

    stack_2 = lay.conv(np.array(stack_1_relu), 32)
    stack_2_maxpool = lay.maxpool(stack_2)
    stack_2_relu = lay.relu(stack_2_maxpool)
    print(stack_2_relu.shape)

    stack_3 = lay.conv(np.array(stack_2_relu), 64)
    stack_3_maxpool = lay.maxpool(stack_3)
    stack_3_relu = lay.relu(stack_3_maxpool)
    print(stack_3_relu.shape)

    flattened = lay.flatten(stack_3_relu)
    print("flattened :", flattened)

    fc_1 = lay.fc(flattened, 128)
    fc_1_relu = lay.relu(fc_1)

    fc_2 = lay.fc(fc_1_relu, 64)
    fc_2_relu = lay.relu(fc_2)

    fc_3 = lay.fc(fc_2_relu, 10)

    print("before softmax values :", fc_3)

    fc_3_softmax = lay.softmax(fc_3)

    print("softmax values :", fc_3_softmax)

    end_time = time.time()

    print("\nTime taken :", end_time-start_time)