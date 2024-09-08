import torch
from torch import tensor
from Helper import ImageLoader, GetModel, Plotter, TrainModel, Json
import os, time

start_time = time.time()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
if device not in ['cuda', 'mps']:
    torch.set_num_threads(8)
    print("Threads set to 8")
print("device", device, "is being used")

conf = {
    'batch_size': 1,
    "l_rate": 0.001,
    "epoch": 5,
    "conv": True,
    "load_jpg": [True, 0.8, "60k"],
}

# Loading Data
data = ImageLoader.load_jpg(conf['load_jpg'][1], "data/input/"+conf['load_jpg'][2], device) if conf['load_jpg'][0] else ImageLoader.load_binary(device)
print("training data shape", data["tensor_data"].shape)
print("testing data shape", data["tensor_test"].shape,'\n')
print("time to load data :", round(time.time()-start_time, 2), '\n')

# Getting model
model = GetModel.model_conv(device) if conf['conv'] else GetModel.model_no_conv(device)

args = "".join(f"_{i}_" for i in conf.values())
model_path = f'data/models/model{args}.pth'
    
# Train if model already doesn't exist
if not os.path.exists(model_path):
    TrainModel.train_model(conf, data, model)
    torch.save(model.state_dict(), model_path)

model.load_state_dict(torch.load(model_path, weights_only=True))

# Testing
model.eval()
test_batch = 100
x = data["tensor_test"]
y = data["tensor_test_labels"]
correct = 0
wrong_indices = []
wrong_lables = []
for i in range(0, x.shape[0], test_batch):
    y_pred = torch.argmax(model(x[i:i+test_batch].unsqueeze(1)), dim=1)
    correct += (torch.sum(y_pred==y[i:i+test_batch]))
    for j in range(len(y_pred)):
        if y_pred[j] != y[i+j]:
            wrong_indices.append(i+j)
            wrong_lables.append(y_pred[j])

Plotter.plot_wrong(x[wrong_indices][:10], wrong_lables[:10], conf)
accuracy = correct/y.shape[0] * 100

print("model accuracy :", accuracy)
print("Total time taken :", time.time() - start_time)

# Add observation to json
Json.add_data(conf, accuracy, start_time)
