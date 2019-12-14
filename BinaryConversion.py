#usr/bin/python3
#-*- coding:utf-8 -*-

import sys
from PyQt5 import QtWidgets

class BinaryConversion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.resize(600, 400)
        self.BinaryConversionUI()
        
    def BinaryConversionUI(self):
        self.HexInputLineEdit = QtWidgets.QLineEdit(self)
        self.HexInputLineEdit.setText("123")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = BinaryConversion()
    test.initUI()
    test.show()
    sys.exit(app.exec_())