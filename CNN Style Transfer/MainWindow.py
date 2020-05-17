from Dialog import Dialog
from Controller import Controller
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.uic as uic

formMain = uic.loadUiType("UI.ui")[0]

class MainWindow(QtWidgets.QMainWindow,formMain):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self,None)
        self.setupUi(self)
        self.Images=[]
        self.GenerateImage=None
        self.Image.setScaledContents(True)
        self.frame.setVisible(False)
        self.TakeImage.triggered.connect(self.TakeImages)
        self.NumStepButton.clicked.connect(self.TakeNumSteps)
        self.SaveImageButton.clicked.connect(self.Save)
        self.ExitButton.clicked.connect(self.Exit)
        self.CancelButton.clicked.connect(self.Cancel)
        self.ExitMenu.triggered.connect(self.Exit)
        self.Control = Controller()

    def ConfirmMode(self):
        if len(self.Images) == 0:
            return
        self.Image.setPixmap(QtGui.QPixmap(self.Images[0][0]).scaled(512,512))
        self.Control.InitializeNetworkImages(self.Images)
        self.Image.setVisible(True)
        self.frame.setVisible(True)
        self.NumStepButton.setVisible(True)
        self.NumStepsBox.setVisible(True)
        self.NumStepsLabel.setVisible(True)
        self.SaveImageButton.setVisible(False)
        self.ExitButton.setVisible(False)
        self.CancelButton.setVisible(False)

    def TakeImages(self):
        dial = Dialog(self)
        dial.show()

    def TakeNumSteps(self):
        self.Control.Network.num_steps = self.NumStepsBox.value()
        self.NumStepButton.setVisible(False)
        self.NumStepsBox.setVisible(False)
        self.NumStepsLabel.setVisible(False)
        self.SaveImageButton.setVisible(True)
        self.ExitButton.setVisible(True)
        self.CancelButton.setVisible(True)
        self.GenerateImage = self.Control.ImageProc.image_show(self.Control.Network.Run_epoch())
        self.Image.setPixmap(QtGui.QPixmap.fromImage(self.GenerateImage))

    def Save(self):
        self.Control.ImageProc.SaveImage(self.GenerateImage)
        self.GenerateImage = None
        self.Image.setVisible(False)
        self.frame.setVisible(False)
        QtWidgets.QMessageBox.information(self,"Информация","Изображение сохранено в папку GeneratedImages")
        self.ConfirmMode()

    def Cancel(self):
        self.GenerateImage = None
        self.Image.setVisible(False)
        self.frame.setVisible(False)
        self.ConfirmMode()

    def Exit(self):
        if QtWidgets.QMessageBox.warning(self,"Предупреждение",
                                         "Приложение закроется без дальнейшего продолжения.\nВас это устраивает?",
                                         QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.No:
            return
        self.close()

app=QtWidgets.QApplication(sys.argv)

Window = MainWindow()
Window.show()

sys.exit(app.exec_())
