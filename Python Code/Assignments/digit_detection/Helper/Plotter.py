import matplotlib.pyplot as plt
import torch

class Plotter:
    def __init__(self):
        pass

    @classmethod
    def plot_epoch(cls, iter_loss, conf):
        args = "".join(f"_{i}_" for i in conf.values())
        plot_path = f'data/output/loss_plot{args}.png'
        plt.plot(range(1,len(iter_loss)+1), iter_loss, marker='o', label='loss')
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.title("Loss per epoch")
        plt.savefig(plot_path)

    @classmethod
    def plot_wrong(cls, images, labels, conf):
        args = "".join(f"_{i}_" for i in conf.values())
        wrong_images = f'data/output/wrong_images{args}.png'
        plt.figure(figsize=(20, 20))
        for i, (image, label) in enumerate(zip(images, labels)):
            plt.subplot(1, len(images), i + 1)
            plt.imshow(image.cpu().numpy())
            plt.title(f'Labeled as : {label.item()}')
            plt.axis('off') 
        plt.savefig(wrong_images)
        plt.close() 
