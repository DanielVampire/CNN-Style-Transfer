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

import os.path

class ConvolutionNeuralNetwork():
    def __init__(self):
        super().__init__()
        self.cnn = models.vgg19(pretrained=True).features.to(device).eval()
        self.cnn_normalization_mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
        self.cnn_normalization_std = torch.tensor([0.229, 0.224, 0.225]).to(device)
        self.content_layers_default = ['conv_15']
        self.style_layers_default = ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5', 'conv_6', 'conv_7', 'conv_8', 'conv_9', 'conv_10', 'conv_11', 'conv_12', 'conv_13', 'conv_14', 'conv_15', 'conv_16']

        self.path = './GeneratedImages/'
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.imsize = 512 if torch.cuda.is_available() else 256
        self.loader = transforms.Compose([transforms.Resize(imsize), transforms.ToTensor()])
        self.unloader = transforms.ToPILImage()
        self.num_steps = 2000
        self.style_weight = 1000000
        self.content_weight = 1

    def image_loader(self, image_name):
        image = Image.open(image_name)
        # fake batch dimension required to fit network's input dimensions
        image = self.loader(image).unsqueeze(0)
        return image.to(device, torch.float)

    def imshow(self, tensor, title=None):
        image = tensor.cpu().clone()  # we clone the tensor to not do changes on it
        image = image.squeeze(0)      # remove the fake batch dimension
        image = self.unloader(image)
        plt.imshow(image)
        if title is not None:
            plt.title(title)
        plt.pause(0.01) # pause a bit so that plots are updated


    def get_style_model_and_losses(self, style_img, content_img, content_layers, style_layers):
        self.cnn = copy.deepcopy(self.cnn)
    
        # normalization module
        normalization = N.Normalization(self.normalization_mean, self.normalization_std).to(device)
    
        # just in order to have an iterable access to or list of content/syle
        # losses
        content_losses = []
        style_losses = []
    
        # assuming that cnn is a nn.Sequential, so we make a new nn.Sequential
        # to put in modules that are supposed to be activated sequentially
        model = nn.Sequential(normalization)
    
        i = 0  # increment every time we see a conv
        for layer in self.cnn.children():
            if isinstance(layer, nn.Conv2d):
                i += 1
                name = 'conv_{}'.format(i)
            elif isinstance(layer, nn.ReLU):
                name = 'relu_{}'.format(i)
                # The in-place version doesn't play very nicely with the
                # ContentLoss
                # and StyleLoss we insert below.  So we replace with
                # out-of-place
                # ones here.
                layer = nn.ReLU(inplace=False)
            elif isinstance(layer, nn.MaxPool2d):
                layer = nn.AvgPool2d(2,2,0)
                name = 'pool_{}'.format(i)
            elif isinstance(layer, nn.BatchNorm2d):
                name = 'bn_{}'.format(i)
            else:
                raise RuntimeError('Unrecognized layer: {}'.format(layer.__class__.__name__))
    
            model.add_module(name, layer)
    
            if name in content_layers:
                # add content loss:
                target = model(content_img).detach()
                content_loss = CL.Content_Loss(target)
                model.add_module("content_loss_{}".format(i), content_loss)
                content_losses.append(content_loss)
    
            if name in style_layers:
                # add style loss:
                target_feature = model(style_img).detach()
                style_loss = SL.Style_Loss(target_feature)
                model.add_module("style_loss_{}".format(i), style_loss)
                style_losses.append(style_loss)
    
        return model, style_losses, content_losses

    def get_input_optimizer(self, input_img):
        # this line to show that input is a parameter that requires a gradient
        optimizer = optim.LBFGS([input_img.requires_grad_()])
        return optimizer

    def run_style_transfer(self, content_img, style_img, input_img):
        """Run the style transfer."""
        print('Building the style transfer model..')
        model, style_losses, content_losses = self.get_style_model_and_losses(style_img, content_img, self.content_layers_default, self.style_layers_default)
        optimizer = self.get_input_optimizer(input_img)
    
        print('Optimizing..')
        run = [0]
        while run[0] <= self.num_steps:
    
            def closure():
                # correct the values of updated input image
                input_img.data.clamp_(0, 1)
    
                optimizer.zero_grad()
                model(input_img)
                style_score = 0
                content_score = 0
    
                for sl in style_losses:
                    style_score += sl.loss
                for cl in content_losses:
                    content_score += cl.loss
    
                style_score *= self.style_weight
                content_score *= self.content_weight
    
                loss = style_score + content_score
                loss.backward()
    
                run[0] += 1
                
                return style_score + content_score
                
            optimizer.step(closure)
    
        # a last correction...
        input_img.data.clamp_(0, 1)
    
        return input_img
    def Run_epoch(self, ContentImage, StyleImage, NumSteps=2000):

        num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

        self.num_steps = NumSteps

        input_img = ContentImage.clone()

        output = self.run_style_transfer(content, style_images[i], input_img, NumSteps)
        
        return output