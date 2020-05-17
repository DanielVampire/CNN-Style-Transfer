import numpy as np
import torch 
from PIL import Image
from PIL.ImageQt import ImageQt
import torchvision.transforms as transforms
from PyQt5 import QtCore, QtGui, QtWidgets
import os.path

class ImageProcessor():
    def __init__(self):
        self.imsize = 512 if torch.cuda.is_available() else 256
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.loader = transforms.Compose([transforms.Resize(self.imsize), transforms.ToTensor()])
        self.unloader = transforms.ToPILImage()
        self.path = './GeneratedImages/'
        self.num_files = len([f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))])
    def image_loader(self, image_name):
        image = Image.open(image_name)
        image = self.loader(image).unsqueeze(0)

        return image.to(self.device, torch.float)
    def image_show(self, tensore):
        Img = tensore.cpu().clone()
        Img = Img.squeeze(0)
        Img = self.unloader(Img)
        Img = ImageQt(Img)
        return Img
    def SaveImage(self,Image):
        Image.save(f'{self.path}{self.num_files}.png')
        self.num_files+=1