### Layers

- Covolve(3,16)
- Maxpool(2,2)
- Relu
- Covolve(16,32)
- Maxpool(2,2)
- Relu
- Covolve(32,64)
- Maxpool(2,2)
- Relu

- Flatten

- Fully Connected(128)
- Relu
- Fully Connected(128,64)
- Relu
- Fully Connected(64,10)
- Output