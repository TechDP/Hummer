#!usr/bin/python3
#-*- coding:utf-8 -*-

import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui

class DeleteBlankLine(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.resize(600, 400)
        self.setWindowTitle("DeleteBlankLine")
        self.DeleteBlankLineUI()

    def DeleteBlankLineUI(self):
        self.PushButtonSelectFile = QtWidgets.QPushButton(self)
        self.PushButtonSelectFile.setText("选择文件")
        self.PushButtonSelectFile.clicked.connect(self.SlotBottonChooseFile)

        self.LineEditShowFilePath = QtWidgets.QLineEdit(self)
        self.LineEditShowFilePath.setReadOnly(True)

        self.GridLayout = QtWidgets.QGridLayout()
        self.GridLayout.addWidget(self.LineEditShowFilePath, 0, 0)
        self.GridLayout.addWidget(self.PushButtonSelectFile, 0, 1)

        self.setLayout(self.GridLayout)
        return self.GridLayout

    def SlotBottonChooseFile(self):
        self.cwd = os.getcwd()
        self.FileNameSelected, filetype = QtWidgets.QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    self.cwd, # 起始路径 
                                    "Text Files (*.txt);;All Files (*)")   # 设置文件扩展名过滤,用双分号间隔

        if self.FileNameSelected == "":
            print("\n取消选择")
            return

        print("\n你选择的文件为:")
        print(self.FileNameSelected)
        print("文件筛选器类型: ",filetype)
        self.LineEditShowFilePath.setText(self.FileNameSelected)
        self.DeleteBlankLineCode()

    def DeleteBlankLineCode(self):
        filename = self.FileNameSelected
        with open(filename,'r') as fr:
            alldata = fr.readlines()
            print(len(alldata))
            with open(self.FileNameSelected + '_done.txt','w') as fw:
                for linedata in alldata:
                    if linedata[0] != '\n':
                        fw.write(linedata)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = DeleteBlankLine()
    test.initUI()
    test.show()
    sys.exit(app.exec_())
