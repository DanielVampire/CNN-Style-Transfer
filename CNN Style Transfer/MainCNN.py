from CNN_Style_Transfer import ConvolutionNeuralNetwork
from Dialog import Dialog
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.uic as uic

formMain = uic.loadUiType("UI.ui")[0]
#CNN = ConvolutionNeuralNetwork()
class MainWindow(QtWidgets.QMainWindow,formMain):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self,None)
        self.setupUi(self)
        self.AvtoBox.setVisible(False)
        self.frame_2.setVisible(False)
        self.Mode=False
        self.AvtoRadioButton.clicked.connect(self.ARB_Openbox)
        self.AvtoBoxButton.clicked.connect(self.AvtoModeTake)
        self.TakeMode.clicked.connect(self.ConfirmMode)
        self.TakeImage.triggered.connect(self.TakeImages)
        self.Image.setPixmap(QtGui.QPixmap("./Images/img2.jpg"))

    def resizeEvent(self,event):
        self.frame.setGeometry(self.width()-181,0,181,self.height())
        self.frame_2.setGeometry(0,self.height()-141,self.width(),121)
        self.Image.setGeometry(0, 0, self.width(), (self.height() - self.frame_2.height()))
        event.accept()

    def ARB_Openbox(self):
        self.AvtoBox.setVisible(True)

    def AvtoModeTake(self):
        #CNN.num_steps = self.NumSteps.value()
        QtWidgets.QMessageBox.information(self,'Message', f'Автоматический режим выбран, число шагов: {CNN.num_steps}')
        self.AvtoBox.setVisible(False)
        self.Mode=True

    def ConfirmMode(self):
        self.frame.setVisible(False)
        #if self.Mode==True:
            #CNN.Run_epoch()
        self.frame_2.setVisible(True)

    def TakeImages(self):
        dial = Dialog()
        dial.show()
        dial.exec_()
app=QtWidgets.QApplication(sys.argv)

Window = MainWindow()
Window.show()

sys.exit(app.exec_())
