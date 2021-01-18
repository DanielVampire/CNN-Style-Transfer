import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.models as models
import copy

import Content_Loss as CL
import Style_Loss as SL
import Normalization as N

class ConvolutionNeuralNetwork():
    def __init__(self):
        super().__init__()
        self.calculationDevice = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.NetworkVGG_19 = models.vgg19(pretrained=True).features.to(self.calculationDevice).eval()

        self.MeanNormalization = torch.tensor([0.485, 0.456, 0.406]).to(self.calculationDevice)
        self.StandartNormalization = torch.tensor([0.229, 0.224, 0.225]).to(self.calculationDevice)

        self.layersForContent = ['convolution 15']
        self.layersForStyle = ['convolution 1', 'convolution 2', 'convolution 3', 'convolution 4', 'convolution 5', 
                               'convolution 6', 'convolution 7', 'convolution 8', 'convolution 9', 'convolution 10',
                              'convolution 11', 'convolution 12', 'convolution 13', 'convolution 14', 'convolution 15', 'convolution 16']
       
        self.ContentImage = None
        self.StyleImage = None

        self.numSteps = 2000
        self.styleProportion = 1000000
        self.contentProportion = 1

    def InitializeContentImage(self,ContentImage):
        self.ContentImage = ContentImage

    def InitializeStyleImage(self,StyleImage):
        self.StyleImage = StyleImage

    def InitializeNormalization(self):
        return N.Normalization(self.MeanNormalization, 
                               self.StandartNormalization).to(self.calculationDevice)

    def InitializeOptimizer(self, Image):
        return optim.LBFGS([Image.requires_grad_()],max_iter=1)

    def InitializeNeuralNetworkAndLoss(self):
        self.NetworkVGG_19 = copy.deepcopy(self.NetworkVGG_19)
    
        listContentLoss = []
        listStyleLoss = []
    
        Network = nn.Sequential(self.InitializeNormalization())
    
        Number = 0 

        for layer in self.NetworkVGG_19.children():

            if isinstance(layer, nn.Conv2d):
                Number += 1
                title = f'convolution {Number}'
            elif isinstance(layer, nn.ReLU):
                title = f'Activation ReLU {Number}'
                layer = nn.ReLU(inplace=False)
            elif isinstance(layer, nn.MaxPool2d):
                layer = nn.AvgPool2d(2,2,0)
                title = f'AveragePool {Number}'

            Network.add_module(title, layer)
    
            if title in self.layersForContent:
                targetImage = Network(self.ContentImage).detach()
                contentLoss = CL.Content_Loss(targetImage)
                Network.add_module(f'Loss Content {Number}', contentLoss)
                listContentLoss.append(contentLoss)

            elif title in self.layersForStyle:
                targetStyle = Network(self.StyleImage).detach()
                styleLoss = SL.Style_Loss(targetStyle)
                Network.add_module(f'style_loss_{Number}', styleLoss)
                listStyleLoss.append(styleLoss)

        return Network, listStyleLoss, listContentLoss

    def Run_epoch(self):

        inputImage = self.ContentImage
        Network, styleLoss, contentLoss = self.InitializeNeuralNetworkAndLoss()
        Optimazer = self.InitializeOptimizer(inputImage)

        Epoch = [0]

        while Epoch[0] <= self.numSteps:
            def closure():
                inputImage.data.clamp_(0, 1)
    
                Optimazer.zero_grad()
                Network(inputImage)
                MeaningStyleLoss = 0
                MeaningContentLoss = 0
    
                for style in styleLoss:
                    MeaningStyleLoss += style.Loss
                for content in contentLoss:
                    MeaningContentLoss += content.Loss
    
                MeaningStyleLoss *= self.styleProportion
                MeaningContentLoss *= self.contentProportion
    
                TotalLoss = MeaningStyleLoss + MeaningContentLoss
                TotalLoss.backward()

                Epoch[0] += 1
                return TotalLoss
                
            Optimazer.step(closure)
            

        inputImage.data.clamp_(0, 1)

        return inputImage