#usr/bin/python3
#-*- coding:utf-8 -*-

import sys
import os
import json
from PyQt5 import QtWidgets

def FormatListToString(DataList):
    tmp = ''
    counter = 0
    
    for i in DataList:
        if counter % 16 == 0:
            tmp += ('\n' + 'addr:0x' + hex(counter + 0x01000000)[2:].zfill(8).upper() + ' ')
        tmp += (str(i).upper() + ' ')
        counter += 1
    return tmp

class BinToString(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.resize(600, 400)
        self.BinToStringUI()

    def BinToStringUI(self):
        # 获取当前程序文件位置
        with open("config.json", 'r') as FileRead:
            ConfigData = FileRead.readline()
            if ConfigData:
                if json.loads(ConfigData)['BinToStringCWD']:
                    self.cwd = json.loads(ConfigData)['BinToStringCWD']
                else:
                    self.cwd = os.getcwd()
            else:
                self.cwd = os.getcwd()
        print(self.cwd)

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
        self.PushButtonIsSaveFile.clicked.connect(self.SlotBottonWriteData)
        
        self.GridLayout = QtWidgets.QGridLayout()
        self.GridLayout.addWidget(self.PushButtonIsSaveFile, 1, 1)
        self.GridLayout.addWidget(self.LineEditShowFilePath, 0, 0)
        self.GridLayout.addWidget(self.ButtonChooseFile, 0, 1)
        self.GridLayout.addWidget(self.TextEditShowFileData, 2, 0, 1, 2)
        self.GridLayout.addWidget(self.LableShowFileCounter, 1, 0)

        self.setLayout(self.GridLayout)
        return self.GridLayout
    


    def TransfromToString(self):
        counter = 0
        fileName = input("输入要转换的文件名称")
        with open(fileName + ".txt", 'w') as fileWrite:
            with open(fileName, 'rb') as fileRead:
                data = fileRead.read(1)
                while data:
                    if counter == 16:
                        fileWrite.write("\n")
                        counter
                    writedata = bytearray(data).hex()
                    fileWrite.write('addr:0x' + writedata + " ")
                    counter += 1
                    data = fileRead.read(1)


    def SlotBottonChooseFile(self):
        self.FileNameSelected, filetype = QtWidgets.QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    self.cwd, # 起始路径 
                                    "Bin Files (*.bin);;All Files (*);;Text Files (*.txt)")   # 设置文件扩展名过滤,用双分号间隔

        if self.FileNameSelected == "":
            print("\n取消选择")
            return
        with open("config.json", 'w') as FileWrite:
            tmp = {}
            tmp["BinToStringCWD"] = self.FileNameSelected
            print("write json data:", tmp["BinToStringCWD"])
            FileWrite.write(json.dumps(tmp))
        print("\n你选择的文件为:")
        print(self.FileNameSelected)
        print("文件筛选器类型: ",filetype)
        self.LineEditShowFilePath.setText(self.FileNameSelected)
        self.ReadBinFile()
        # self.TextEditShowFileData.setText(FormatListToString(self.FileData))
        self.LableShowFileCounter.setText("字节数：" + str(self.FileDataCounter))

    def SlotBottonWriteData(self):
        if not self.LineEditShowFilePath.text():
            self.TextEditShowFileData.setText("请先选择文件！")
            return 
        self.WriteStringFile(FormatListToString(self.FileData))

    def ReadBinFile(self):
        self.FileData = []
        self.FileDataCounter = 0
        with open(self.FileNameSelected, 'rb') as fileRead:
            data = fileRead.read(1)
            while data:
                self.FileDataCounter += 1
                self.FileData.append(bytearray(data).hex())
                data = fileRead.read(1)
        print(self.FileData)
        print(self.FileDataCounter)

    def WriteStringFile(self, WriteData):
        with open(self.FileNameSelected + ".txt", 'w') as FileWrite:
            FileWrite.write(WriteData)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = BinToString()
    test.initUI()
    test.show()
    sys.exit(app.exec_())