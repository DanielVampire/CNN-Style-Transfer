from Neural_Network import ConvolutionNeuralNetwork
from ImageProcessor import ImageProcessor

class Controller():
    def __init__(self):
        self.Network = ConvolutionNeuralNetwork()
        self.ImageProc = ImageProcessor()

    def SetNumSteps(self,NumSteps):
        self.Network.numSteps = NumSteps

    def InitializeNetworkImages(self, Images):
        check=True
        for j in Images[0]:
            if Images[0].index(j)==0 and check:
                self.Network.InitializeContentImage(self.ImageProc.imageToTensor(j))
                check=False
            else:
                self.Network.InitializeStyleImage(self.ImageProc.imageToTensor(j))
                if Images[0].index(j) == (len(Images[0])-1):
                    Images.remove(Images[0])
                    break
                else:
                    Images[0].remove(j)
                    break

    def RunNetwork(self):
        return self.ImageProc.tensorToImage(self.Network.Run_epoch())

    def SaveImage(self, image):
        self.ImageProc.SaveImage(image)


