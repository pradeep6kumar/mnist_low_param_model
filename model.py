import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        dropout_value = 0.1
        
        # Initial Depthwise Block
        self.depthwise1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=8, kernel_size=(3, 3), 
                     padding=1, groups=1, bias=False),
            nn.BatchNorm2d(8),
            nn.ReLU(),
            nn.Dropout(dropout_value)
        ) # output_size = 28

        # Second Depthwise Block
        self.depthwise2 = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=16, kernel_size=(3, 3), 
                     padding=1, groups=8, bias=False),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Dropout(dropout_value)
        ) # output_size = 28

        # Transition Block 1
        self.transition1 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=8, kernel_size=(1, 1), 
                     padding=0, bias=False),
            nn.MaxPool2d(2, 2)
        ) # output_size = 14

        # Convolution Block 1
        self.convblock1 = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=16, kernel_size=(3, 3), 
                     padding=1, bias=False),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Dropout(dropout_value)
        ) # output_size = 14

        # Transition Block 2
        self.transition2 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=8, kernel_size=(1, 1), 
                     padding=0, bias=False),
            nn.MaxPool2d(2, 2)
        ) # output_size = 7

        # Convolution Block 2
        self.convblock2 = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=16, kernel_size=(3, 3), 
                     padding=1, bias=False),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.Dropout(dropout_value)
        ) # output_size = 7

        # Global Average Pooling
        self.gap = nn.Sequential(
            nn.AvgPool2d(kernel_size=7)
        ) # output_size = 1

        # Final 1x1 convolution
        self.convblock3 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=10, kernel_size=(1, 1), 
                     padding=0, bias=False)
        )

    def forward(self, x):
        x = self.depthwise1(x)
        x = self.depthwise2(x)
        x = self.transition1(x)
        x = self.convblock1(x)
        x = self.transition2(x)
        x = self.convblock2(x)
        x = self.gap(x)
        x = self.convblock3(x)
        x = x.view(-1, 10)
        return F.log_softmax(x, dim=-1) 