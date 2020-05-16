from CNN_Style_Transfer import ConvolutionNeuralNetwork
from ImageProcessor import ImageProcessor

class Controller():
    def __init__(self):
        self.Network = ConvolutionNeuralNetwork()
        self.ImageProc = ImageProcessor()
    def SetNumSteps(self,NumSteps):
        self.Network.num_steps = NumSteps
    def InitializeNetwork(self, Images):
        for j in Images[0]:
            if Images[0].index(j)==0:
                self.Network.InitializeContentImage(self.ImageProc.image_loader(j))
            else:
                self.Network.InitializeStyleImage(j)
                if Images[0].index(j) == (len(Images[0])-1):
                    Images.remove(Images[0])
                    break
                else:
                    Images[0].remove(j)
                    break
        self.Network.InitializeNormalization()
        self.Network.InitializeModelAndLosses()
        self.Network.InitializeOptimizer()
    def RunNetwork(self):
        return self.Network.Run_epoch()


