import torch
import torch.nn as nn
import torch.nn.functional as Functional


class Content_Loss(nn.Module):

    def __init__(self, target,):
        super(Content_Loss, self).__init__()
        # we 'detach' the target content from the tree used
        # to dynamically compute the gradient: this is a stated value,
        # not a variable. Otherwise the forward method of the criterion
        # will throw an error.
        self.target = target.detach()

    def forward(self, input):
        self.loss = Functional.mse_loss(input, self.target)
        return input
