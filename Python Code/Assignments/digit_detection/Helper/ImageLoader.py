import idx2numpy
import torch
import numpy as np
from PIL import Image
import os

class ImageLoader:
    def __init__(self) -> None:
        pass


    @classmethod
    def load_jpg(cls, split, path, device):
        images = []
        labels = []
        for i in os.listdir(path):
            for j in os.listdir(path + f'/{i}'):
                img = Image.open(path+f'/{i}'+f'/{j}').convert("L")
                images.append(torch.tensor(np.array(img)).float())
                labels.append(int(i))
        images = torch.stack(images)
        labels = torch.tensor(labels)
        data_dict = {}
        index = torch.randperm(len(images))
        images, labels = images[index], labels[index]
        r = int(images.shape[0]*split)
        data_dict["tensor_data"] = images[:r].clone().detach().to(device)
        data_dict["tensor_data_labels"] = labels[:r].clone().detach().to(device)
        data_dict["tensor_test"] = images[r:].clone().detach().to(device)
        data_dict["tensor_test_labels"] = labels[r:].clone().detach().to(device)

        return data_dict

    @classmethod
    def load_binary(cls, device):
        file_path_img = 'data/input/train-images-idx3-ubyte'
        file_path_img_label = 'data/input/train-labels-idx1-ubyte'
        file_path_test = 'data/input/t10k-images.idx3-ubyte'
        file_path_test_label = 'data/input/t10k-labels.idx1-ubyte'

        data = idx2numpy.convert_from_file(file_path_img)
        labels = idx2numpy.convert_from_file(file_path_img_label)
        test_data = idx2numpy.convert_from_file(file_path_test)
        test_labels = idx2numpy.convert_from_file(file_path_test_label)

        data_dict = {}

        data_dict["tensor_data"] = torch.from_numpy(np.copy(data)).float().to(device)
        data_dict["tensor_data_labels"] = torch.from_numpy(np.copy(labels)).to(device)
        data_dict["tensor_test"] = torch.from_numpy(np.copy(test_data)).float().to(device)
        data_dict["tensor_test_labels"] = torch.from_numpy(np.copy(test_labels)).to(device)

        return data_dict