from __future__ import print_function

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from PIL import Image
import matplotlib.pyplot as plt

import torchvision.transforms as transforms
import torchvision.models as models

import copy

import Content_Loss as CL
import Style_Loss as SL
import Normalization as N



class ConvolutionNeuralNetwork():
    def __init__(self):
        super().__init__()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.cnn = models.vgg19(pretrained=True).features.to(self.device).eval()

        self.cnn_normalization_mean = torch.tensor([0.485, 0.456, 0.406]).to(self.device)
        self.cnn_normalization_std = torch.tensor([0.229, 0.224, 0.225]).to(self.device)

        self.content_layers_default = ['conv_15']
        self.style_layers_default = ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5', 'conv_6', 'conv_7', 'conv_8', 'conv_9', 'conv_10', 'conv_11', 'conv_12', 'conv_13', 'conv_14', 'conv_15', 'conv_16']
       
        self.ContentImage = None
        self.StyleImage = None

        self.num_steps = 2000
        self.style_weight = 1000000
        self.content_weight = 1

    def InitializeContentImage(self,ContentImage):
        self.ContentImage = ContentImage
    def InitializeStyleImage(self,StyleImage):
        self.StyleImage = StyleImage

    def InitializeNormalization(self):
        return N.Normalization(self.cnn_normalization_mean, self.cnn_normalization_std).to(self.device)

    def InitializeModelAndLosses(self):
        self.cnn = copy.deepcopy(self.cnn)
    
        Content_Loss = []
        Style_Loss = []
    
        Model = nn.Sequential(self.InitializeNormalization())
    
        i = 0 
        for layer in self.cnn.children():
            if isinstance(layer, nn.Conv2d):
                i += 1
                name = 'conv_{}'.format(i)
            elif isinstance(layer, nn.ReLU):
                name = 'relu_{}'.format(i)
                layer = nn.ReLU(inplace=False)
            elif isinstance(layer, nn.MaxPool2d):
                layer = nn.AvgPool2d(2,2,0)
                name = 'pool_{}'.format(i)
            elif isinstance(layer, nn.BatchNorm2d):
                name = 'bn_{}'.format(i)
            else:
                raise RuntimeError('Unrecognized layer: {}'.format(layer.__class__.__name__))
    
            Model.add_module(name, layer)
    
            if name in self.content_layers_default:
                target = Model(self.ContentImage).detach()
                content_loss = CL.Content_Loss(target)
                Model.add_module("content_loss_{}".format(i), content_loss)
                Content_Loss.append(content_loss)
    
            if name in self.style_layers_default:
                target_feature = Model(self.StyleImage).detach()
                style_loss = SL.Style_Loss(target_feature)
                Model.add_module("style_loss_{}".format(i), style_loss)
                Style_Loss.append(style_loss)

        return Model,Style_Loss,Content_Loss

    def InitializeOptimizer(self, Image):
        return optim.LBFGS([Image.requires_grad_()])

    def Run_epoch(self):


        input_img = self.ContentImage
        model,style_loss,content_loss = self.InitializeModelAndLosses()
        Optimazer = self.InitializeOptimizer(input_img)
        print('Optimizing..')
        run = [0]
        while run[0] <= self.num_steps:
            def closure():
                input_img.data.clamp_(0, 1)
    
                Optimazer.zero_grad()
                model(input_img)
                style_score = 0
                content_score = 0
    
                for sl in style_loss:
                    style_score += sl.loss
                for cl in content_loss:
                    content_score += cl.loss
    
                style_score *= self.style_weight
                content_score *= self.content_weight
    
                loss = style_score + content_score
                loss.backward()
    
                run[0] += 1
                
                return style_score + content_score
                
            Optimazer.step(closure)

        input_img.data.clamp_(0, 1)

        return input_img