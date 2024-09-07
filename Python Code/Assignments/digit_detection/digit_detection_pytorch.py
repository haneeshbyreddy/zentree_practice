import numpy as np
import torch
from torch import nn, tensor, optim
from Helper import ImageLoader, GetModel, Plotter
import matplotlib.pyplot as plt
import os
import json
import time

start_time = time.time()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
print("device", device, "is being used")

conf = {
    'batch_size': 10,
    "l_rate": 0.001,
    "epoch": 10,
    "conv": True,
    "load_jpg": [True, 0.8, "60k"],
}

data = ImageLoader.load_jpg(conf['load_jpg'][1], "data/input/"+conf['load_jpg'][2], device) if conf['load_jpg'][0] else ImageLoader.load_binary(device)
print("training data shape", data["tensor_data"].shape)
print("testing data shape", data["tensor_test"].shape,'\n')

model = GetModel.model_conv(device) if conf['conv'] else GetModel.model_no_conv(device)

args = "".join(f"_{i}_" for i in conf.values())
model_path = f'data/models/model{args}.pth'

re_train = False
if os.path.exists(model_path):
    re_train = bool(input("Model already available do you want to re_train [y/n]:") == 'y')
    
if re_train or not os.path.exists(model_path):
    loss_fn = nn.CrossEntropyLoss()
    optimzer = optim.Adam(model.parameters(), lr=conf['l_rate'])

    model.train()
    iter_loss = []
    for epoch in range(conf['epoch']):
        iter_loss.append(0)
        for i in range(0, data["tensor_data"].shape[0], conf['batch_size']):
            optimzer.zero_grad()
            x_batch = data["tensor_data"][i:i+conf['batch_size']]
            y_pred = x_batch.unsqueeze(1) if conf['conv'] else x_batch
            for layer in model:
                y_pred = layer(y_pred)
            y_batch = data["tensor_data_labels"][i:i+conf['batch_size']]
            loss = loss_fn(y_pred, y_batch)
            iter_loss[-1] += loss.item()
            loss.backward()
            optimzer.step()
        print(f'epoch :{epoch}, loss :{iter_loss[-1]}')
    Plotter.plot_epoch(iter_loss)
    torch.save(model.state_dict(), model_path)

model.load_state_dict(torch.load(model_path, weights_only=True))

# Testing
model.eval()
test_batch = 100
x = data["tensor_test"]
y = data["tensor_test_labels"]
correct = 0
wrong_indices = []
for i in range(0, x.shape[0], test_batch):
    y_pred = torch.argmax(model(x[i:i+test_batch].unsqueeze(1)), dim=1)
    correct += (torch.sum(y_pred==y[i:i+test_batch]))
    for j in range(len(y_pred)):
        if y_pred[j] != y[i+j]:
            wrong_indices.append(i+j)

Plotter.plot_wrong(x[wrong_indices][:10], y[wrong_indices][:10])
accuracy = correct/y.shape[0] * 100

print("model accuracy :", accuracy)

# Adding results to json file
json_file = "data/accuracy.json"
with open(json_file, mode='r', encoding='utf-8') as read_file:
    json_arr = json.load(read_file)
    conf_exists = False
    for entry in json_arr:
        if {k: entry[k] for k in conf} == conf:
            entry['accuracy'].append(accuracy.item())
            entry['time_taken'] = time.time() - start_time
            conf_exists = True
            break
    if not conf_exists:
        json_arr.append(conf | {'accuracy': [accuracy.item()]})
with open(json_file, mode='w', encoding='utf-8') as write_file:
    json.dump(json_arr, write_file, skipkeys=True)
