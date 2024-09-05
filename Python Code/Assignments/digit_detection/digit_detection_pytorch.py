import numpy as np
import torch
from torch import nn, tensor, optim
from Helper import ImageLoader
import os

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print("device", device, "is being used")

conf = {
    'batch_size': 40,
    "l_rate": 0.001,
    "epoch": 80,
    "conv": False,
    "load_jpg": [True, 0.8],
}

data = ImageLoader.load_jpg(conf['load_jpg'][1], device) if conf['load_jpg'][0] else ImageLoader.load_binary(device)

print("training data shape", data["tensor_data"].shape)
print("testing data shape", data["tensor_test"].shape,'\n')

args = "".join(f"_{i}_" for i in conf.values())
model_path = f'data/models/model{args}.pth'

model_conv = nn.Sequential(
    nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=1).to(device),
    nn.MaxPool2d(kernel_size=2, stride=1).to(device),
    nn.ReLU(),
    nn.Conv2d(in_channels=16, out_channels=32, kernel_size=5, stride=1).to(device),
    nn.MaxPool2d(kernel_size=2, stride=1).to(device),
    nn.ReLU(),
    nn.Conv2d(in_channels=32, out_channels=64, kernel_size=7, stride=1).to(device),
    nn.MaxPool2d(kernel_size=2, stride=1).to(device),
    nn.ReLU(),
    nn.Flatten().to(device),
    nn.Linear(64*13*13, 128).to(device),
    nn.Sigmoid().to(device),
    nn.Linear(128, 64).to(device),
    nn.Sigmoid().to(device),
    nn.Linear(64, 10).to(device),
)

model_no_conv = nn.Sequential(
    nn.Flatten().to(device),
    nn.Linear(784, 128).to(device),
    nn.Sigmoid().to(device),
    nn.Linear(128, 64).to(device),
    nn.Sigmoid().to(device),
    nn.Linear(64, 10).to(device),
)

model = model_conv if conf['conv'] else model_no_conv
re_train = False
if os.path.exists(model_path):
    re_train = bool(input("Model already available do you want to re_train [y/n]:") == 'y')
if re_train or not os.path.exists(model_path):
    loss_fn = nn.CrossEntropyLoss()
    optimzer = optim.Adam(model.parameters(), lr=conf['l_rate'])

    model.train()
    for epoch in range(conf['epoch']):
        iter_loss = 0
        for i in range(0, data["tensor_data"].shape[0], conf['batch_size']):
            optimzer.zero_grad()
            x_batch = data["tensor_data"][i:i+conf['batch_size']]
            y_pred = x_batch.unsqueeze(1) if conf['conv'] else x_batch
            for layer in model:
                y_pred = layer(y_pred)
            y_batch = data["tensor_data_labels"][i:i+conf['batch_size']]
            loss = loss_fn(y_pred, y_batch)
            iter_loss += loss.item()
            loss.backward()
            optimzer.step()
        print(f'epoch :{epoch}, loss :{iter_loss}')
    torch.save(model.state_dict(), model_path)

model.load_state_dict(torch.load(model_path, weights_only=True))

# Testing

model.eval()
test_batch = 100
x = data["tensor_test"]
y = data["tensor_test_labels"]
correct = 0
for i in range(0, x.shape[0], test_batch):
    y_pred = torch.argmax(model(x[i:i+test_batch].unsqueeze(1)), dim=1)
    correct += (torch.sum(y_pred==y[i:i+test_batch]))
accuracy = correct/x.shape[0] * 100

print("model accuracy :", accuracy)