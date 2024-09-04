import numpy as np
import torch
from torch import nn, tensor, optim
import idx2numpy
import os

file_path_img = 'data/input/train-images-idx3-ubyte'
file_path_img_label = 'data/input/train-labels-idx1-ubyte'
file_path_test = 'data/input/t10k-images.idx3-ubyte'
file_path_test_label = 'data/input/t10k-labels.idx1-ubyte'

data = idx2numpy.convert_from_file(file_path_img)
labels = idx2numpy.convert_from_file(file_path_img_label)
test_data = idx2numpy.convert_from_file(file_path_test)
test_labels = idx2numpy.convert_from_file(file_path_test_label)

tensor_data = torch.from_numpy(np.copy(data)).float()
tensor_data_labels = torch.from_numpy(np.copy(labels))
tensor_test = torch.from_numpy(np.copy(test_data)).float()
tensor_test_labels = torch.from_numpy(np.copy(test_labels))

model_path = 'data/model.pth'

model = nn.Sequential(
    # nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3)
    # nn.maxpool()
    nn.Flatten(),
    nn.Linear(784, 128),
    nn.Sigmoid(),
    nn.Linear(128, 64),
    nn.Sigmoid(),
    nn.Linear(64, 10),
)

if not os.path.exists(model_path):
    loss_fn = nn.CrossEntropyLoss()
    optimzer = optim.Adam(model.parameters(), lr=0.001)
    batch_size = 10

    model.train()
    for epoch in range(5):
        for i in range(0, tensor_data.shape[0], batch_size):
            optimzer.zero_grad()
            x_batch = tensor_data[i:i+batch_size]
            y_pred = model(x_batch)
            y_batch = tensor_data_labels[i:i+batch_size]
            loss = loss_fn(y_pred, y_batch)
            loss.backward()
            optimzer.step()
    torch.save(model.state_dict(), model_path)

model.load_state_dict(model_path)

model.eval()
count = 0
for i in range(tensor_test.shape[0]):
    x = tensor_test[i].unsqueeze(0)
    y = tensor_test_labels[i]
    y_pred = model(x)
    if torch.argmax(y_pred) == y:
        count += 1

print("model accuracy :", (count/10000)*100)