import torch
import torch.nn as nn
import torch.nn.functional as Functional


class Content_Loss(nn.Module):

    def __init__(self, targetImage):
        super(Content_Loss, self).__init__()
        self.target = targetImage.detach()

    def forward(self, image):
        self.Loss = Functional.mse_loss(image, self.target)
        return image
