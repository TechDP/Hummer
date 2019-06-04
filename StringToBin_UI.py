#usr/bin/python3
#-*- coding:utf-8 -*-

import sys
import os
from PyQt5 import QtWidgets

class StringToBin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.resize(600, 400)
        self.BinToStringUI()

    def BinToStringUI(self):
        # 获取当前程序文件位置
        self.cwd = os.getcwd()

        # 创建一个按钮，点击后触发 chooseFile 槽
        self.ButtonChooseFile = QtWidgets.QPushButton(self)
        self.ButtonChooseFile.setText("选择文件")
        self.ButtonChooseFile.clicked.connect(self.SlotBottonChooseFile)

        # 创建一个单行文本框显示文件目录
        self.LineEditShowFilePath = QtWidgets.QLineEdit(self)
        self.LineEditShowFilePath.setReadOnly(True)
        
        # 创建一个多行文本框显示文件数据
        self.TextEditShowFileData = QtWidgets.QTextEdit(self)

        # 创建一个 lable 显示文件字节数
        self.LableShowFileCounter = QtWidgets.QLabel(self)

        self.PushButtonIsSaveFile = QtWidgets.QPushButton(self)
        self.PushButtonIsSaveFile.setText("保存到文件")
        self.PushButtonIsSaveFile.clicked.connect(self.TransFormToBinAndWriteFile)
        
        self.GridLayout = QtWidgets.QGridLayout()
        self.GridLayout.addWidget(self.PushButtonIsSaveFile, 1, 1)
        self.GridLayout.addWidget(self.LineEditShowFilePath, 0, 0)
        self.GridLayout.addWidget(self.ButtonChooseFile, 0, 1)
        self.GridLayout.addWidget(self.TextEditShowFileData, 2, 0, 1, 2)
        self.GridLayout.addWidget(self.LableShowFileCounter, 1, 0)

        self.setLayout(self.GridLayout)
        return self.GridLayout

    def SlotBottonChooseFile(self):
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
        # with open(self.FileNameSelected, 'r') as FileRead:
        #     self.TextEditShowFileData.setText(FileRead.readline())
        # self.TransFormToBinAndWriteFile(self.FileNameSelected)

    def TransFormToBinAndWriteFile(self):
        if not self.LineEditShowFilePath.text():
            self.TextEditShowFileData.setText("请先选择文件！")
            return
        with open(self.FileNameSelected,'r') as fr:
            alldata = fr.read()
            with open(self.FileNameSelected + '.bin','ab') as fw:
                fw.write(bytearray.fromhex(alldata))
        self.TextEditShowFileData.setText("转换完成。")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = StringToBin()
    test.initUI()
    test.show()
    sys.exit(app.exec_())