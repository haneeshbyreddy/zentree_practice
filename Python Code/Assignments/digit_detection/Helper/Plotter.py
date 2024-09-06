import matplotlib.pyplot as plt
import torch

class Plotter:
    def __init__(self):
        pass

    @classmethod
    def plot_epoch(cls, iter_loss):
        model_path = 'data/output/loss_plot.png'
        plt.plot(range(1,len(iter_loss)+1), iter_loss, marker='o', label='loss')
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.title("Loss per epoch")
        plt.savefig(model_path)

    @classmethod
    def plot_wrong(cls, images, labels):
        wrong_images = 'data/output/wrong_images.png'
        plt.figure(figsize=(20, 20))
        for i, (image, label) in enumerate(zip(images, labels)):
            plt.subplot(1, len(images), i + 1)
            plt.imshow(image.cpu().numpy())
            plt.title(f'Labeled as : {label.item()}')
            plt.axis('off') 
        plt.savefig(wrong_images)
        plt.close() 
