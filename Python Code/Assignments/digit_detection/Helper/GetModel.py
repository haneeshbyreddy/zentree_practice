from torch import nn

class GetModel:
    def __init__(self) -> None:
        pass

    @classmethod
    def model_conv(cls, device):
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
        return model_conv
    
    @classmethod
    def model_no_conv(cls, device):
        model_no_conv = nn.Sequential(
            nn.Flatten().to(device),
            nn.Linear(784, 128).to(device),
            nn.Sigmoid().to(device),
            nn.Linear(128, 64).to(device),
            nn.Sigmoid().to(device),
            nn.Linear(64, 10).to(device),
        )
        return model_no_conv