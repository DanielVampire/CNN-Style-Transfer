import torch
import torch.nn as nn

class Normalization(nn.Module):
    def __init__(self, meanValue, standartValue):
        super(Normalization, self).__init__()

        self.meanNorm = meanValue.view(-1, 1, 1)
        self.stdNorm = standartValue.view(-1, 1, 1)

    def forward(self, Image):
        value = (Image - self.meanNorm) / self.stdNorm
        return value