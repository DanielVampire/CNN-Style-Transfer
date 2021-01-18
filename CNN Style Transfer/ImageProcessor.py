import numpy as np
import torch 
from PIL import Image
from PIL.ImageQt import ImageQt
import torchvision.transforms as transforms
from PyQt5 import QtCore, QtGui, QtWidgets
import os.path
import os

class ImageProcessor():
    def __init__(self):
        self.SizeImage = 512 if torch.cuda.is_available() else 256
        self.calculationDevice = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.toTensor = transforms.Compose([transforms.Resize(self.SizeImage), transforms.ToTensor()])
        self.toPilImage = transforms.ToPILImage()

        self.path = './GeneratedImages/'

        if os.path.isdir('./GeneratedImages/'):
            self.path = self.path
        else:
            os.mkdir(self.path)
            self.path = self.path

        self.num_files = len([f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))])

    def imageToTensor(self, imagePath):
        Img = Image.open(imagePath)
        Img = self.toTensor(Img).unsqueeze(0)

        return Img.to(self.calculationDevice, torch.float)

    def tensorToImage(self, tensore):
        Img = tensore.cpu().clone()
        Img = Img.squeeze(0)
        Img = self.toPilImage(Img)
        Img = ImageQt(Img)
        return Img

    def SaveImage(self,Image):
        Image.save(f'{self.path}{self.num_files}.png')
        self.num_files+=1