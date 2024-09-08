from torch import optim, nn, tensor
import time
from Helper import Plotter

class TrainModel:
    def __init__(self) -> None:
        pass

    @classmethod
    def train_model(cls, conf, data, model):
        loss_fn = nn.CrossEntropyLoss()
        optimzer = optim.Adam(model.parameters(), lr=conf['l_rate'])

        model.train()
        iter_loss = []
        for epoch in range(conf['epoch']):
            before_epoch = time.time()
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
            print(f'epoch :{epoch}, loss :{iter_loss[-1]}, time :{round(time.time() - before_epoch, 2)}')
        Plotter.plot_epoch(iter_loss, conf)
