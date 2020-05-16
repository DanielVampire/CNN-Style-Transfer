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
        self.AvtoBox.setVisible(False)
        self.frame_2.setVisible(False)
        self.Images=[]
        self.AvtoRadioButton.clicked.connect(self.ARB_Openbox)
        self.AvtoBoxButton.clicked.connect(self.AvtoModeTake)
        self.ManualRadioButton.clicked.connect(self.ManualMode)
        self.OneStepButton.clicked.connect(self.OneStep)
        self.TenStepButton.clicked.connect(self.TenStep)
        self.HundredStepButton.clicked.connect(self.HundredStep)
        self.ThousandStepButton.clicked.connect(self.ThousandStep)

        self.TakeMode.clicked.connect(self.ConfirmMode)
        self.TakeImage.triggered.connect(self.TakeImages)
        self.Control = Controller()

    def resizeEvent(self,event):
        self.frame.setGeometry(self.width()-181,0,181,self.height())
        self.frame_2.setGeometry(0,self.height()-141,self.width(),121)
        self.Image.setGeometry(0, 0, self.width(), (self.height() - self.frame_2.height()))
        event.accept()
    def ARB_Openbox(self):
        self.AvtoBox.setVisible(True)

    def AvtoModeTake(self):
        QtWidgets.QMessageBox.information(self,'Message', f'Автоматический режим выбран, число шагов: {self.NumSteps.value()}')
        self.AvtoBox.setVisible(False)
        self.Control.SetNumSteps(self.NumSteps.value())

    def ManualMode(self):
        QtWidgets.QMessageBox.information(self,'Message', 'Выбран ручной режим')

    def ConfirmMode(self):
        self.frame.setVisible(False)
        self.frame_2.setVisible(True)
        self.Image.setPixmap(QtGui.QPixmap(self.Images[0][0]))
        self.Control.InitializeNetwork(self.Images)
    def TakeImages(self):
        dial = Dialog(self)
        dial.show()

    def OneStep(self):
        self.Control.SetNumSteps(1)
        self.Control.RunNetwork()
    def TenStep(self):
        self.Control.SetNumSteps(10)
        self.Control.RunNetwork()
    def HundredStep(self):
        self.Control.SetNumSteps(100)
        self.Control.RunNetwork()
    def ThousandStep(self):
        self.Control.SetNumSteps(1000)
        self.Control.RunNetwork()
app=QtWidgets.QApplication(sys.argv)

Window = MainWindow()
Window.show()

sys.exit(app.exec_())
