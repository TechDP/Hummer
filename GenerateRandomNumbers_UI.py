#!usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import random, time
from PyQt5 import QtWidgets, QtCore, QtGui

class GenerateRandom(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.initUI()

    def initUI(self):
        
        self.resize(600, 400)
        self.setWindowTitle("生成随机数")
        self.move(20, 50)
        self.StackGenerateRandomNumbersUI()

    def StackGenerateRandomNumbersUI(self):
        print("StackGenerateRandomNumbersUI in")
        # 生成一个按钮
        self.PushButtonGenerateRandomNumbers = QtWidgets.QPushButton("生成随机数", self)
        self.PushButtonGenerateRandomNumbers.clicked.connect(self.GenerateRandomNumbersIRQ)

        # 生成一个 lineEdit 获取数量
        self.LineEditGetNumber = QtWidgets.QLineEdit(self)
        # 限制单行文本输入框输入
        self.pIntValidator = QtGui.QIntValidator(self)
        self.pIntValidator.setRange(1, 100000)
        self.LineEditGetNumber.setValidator(self.pIntValidator)
        self.LineEditGetNumber.setPlaceholderText(str(256))

        # 生成一个复选框选择是否保存到文件
        self.CheckBoxIsSaveTandomToFile = QtWidgets.QCheckBox("是否保存到文件", self)

        # 生成一个文本框显示随机数
        self.TextEditRandomData = QtWidgets.QTextEdit(self)

        self.GridLayoutGenerateRandom = QtWidgets.QGridLayout(self)
        self.GridLayoutGenerateRandom.addWidget(self.CheckBoxIsSaveTandomToFile, 0, 0, 1, 1)
        self.GridLayoutGenerateRandom.addWidget(self.LineEditGetNumber, 1, 0, 1, 1)
        self.GridLayoutGenerateRandom.addWidget(self.PushButtonGenerateRandomNumbers, 1, 10, 1, 1)
        self.GridLayoutGenerateRandom.addWidget(self.TextEditRandomData, 2, 0, 1, 20)

        print("StackGenerateRandomNumbersUI out")
        return self.GridLayoutGenerateRandom

    def GenerateRandomNumbersIRQ(self):
        if self.LineEditGetNumber.text():
            number = int(self.LineEditGetNumber.text())
        else:
            number = 256
        self.RandomData = self.GenerateRandomNumbers(number)
        print("生成随机数")
        self.TextEditRandomData.setText(self.RandomData)
        if self.CheckBoxIsSaveTandomToFile.isChecked():
            print("把随机数写入到文件")
            self.RandomDataWriteToFile(self.RandomData)
        
        

    def GenerateRandomNumbers(self, number):
        counter = 0
        tmp = ""
        while counter < number:
            counter += 1
            databyte = hex(random.randint(0,255))
            if len(databyte) == 3:
                databyte = databyte[0 : 2] + '0' + databyte[2 : ]
            tmp = tmp + databyte + ', '
            if counter % 16 == 0:
                tmp = tmp + "\n"
        return tmp

    def RandomDataWriteToFile(self, strdata):
        with open("data.txt", 'w') as filewrite:
            print("write File")
            filewrite.write(strdata)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = GenerateRandom()
    ex.initUI()
    ex.show()
    
    sys.exit(app.exec_())
