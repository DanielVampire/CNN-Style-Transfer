import torch
import torch.nn as nn
import torch.nn.functional as Functional


class Style_Loss(nn.Module):

    def __init__(self, targetStyle):
        super(Style_Loss, self).__init__()
        self.target = self.MatrixGram(targetStyle).detach()

    def forward(self, Image):
        Matrix = self.MatrixGram(Image)
        self.Loss = Functional.mse_loss(Matrix, self.target)
        return Image

    def MatrixGram(self,input):
        batchSize, ColorChannel, Width, Height = input.size()  

        VectorSys = input.view(batchSize * ColorChannel, Width * Height)  

        Matrix = torch.mm(VectorSys, VectorSys.t())  

        return Matrix.div(batchSize * ColorChannel * Width * Height)
