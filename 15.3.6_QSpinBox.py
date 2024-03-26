import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        label = QLabel("메도수량: ", self)
        label.move(10, 20)

        self.spinBox = QSpinBox(self)
        self.spinBox.move(70, 75)
