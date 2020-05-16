import numpy as np
import torch 
from PIL import Image
import torchvision.transforms as transforms

class ImageProcessor():
    def __init__(self):
        self.imsize = 512 if torch.cuda.is_available() else 256
        self.loader = transforms.Compose([transforms.Resize(self.imsize), transforms.ToTensor()])
        self.unloader = transforms.ToPILImage()

    def image_loader(self, image_name):
        image = Image.open(image_name)
        image = self.loader(image).unsqueeze(0)

        return image.to(self.device, torch.float)
    
    def TensoreToNumpy(self,tensore):
        Img = tensore.cpu().clone()
        Img = Img.numpy()
        Img.astype(np.uint8)

        return Img
    def NumpyToQImage(self,Image):
        pass