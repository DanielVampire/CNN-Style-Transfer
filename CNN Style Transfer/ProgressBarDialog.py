from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.uic as uic

dialogForm = uic.loadUiType("ProgressBar.ui")[0]

class ProgressBarDialog(QtWidgets.QWidget, dialogForm):
    def __init__(self,parent = None):
        super().__init__(parent,QtCore.Qt.Window)
        self.setupUi(self)

