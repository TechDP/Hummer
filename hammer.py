#usr/bin/python3
# -*- coding:utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from GenerateRandomNumbers_UI import GenerateRandom
from BinToString_UI import BinToString
from DeleteBlankLine_UI import DeleteBlankLine
from StringToBin_UI import StringToBin

class Hammer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        # self.resize(900, 500)
        # 设置窗口大小 且不可拖动改变
        self.setFixedSize(900, 500)
        self.setMinimumHeight(500)
        self.setMinimumWidth(900)
        self.setWindowTitle("Hammer")
        self.mainUI()
        
    
    def mainUI(self):
        # 创建左侧列表
        self.leftlist = QtWidgets.QListWidget(self)
        # 左侧列表被选后发送信号给 display 槽
        self.leftlist.currentRowChanged.connect(self.display)

        # 创建右侧 widget
        self.RightStack = QtWidgets.QStackedWidget(self)

        # 实例化随机数类
        self.GenerateRandom = GenerateRandom()
        # 创建 QWidget 添加随机数实例
        self.stackRandom = QtWidgets.QWidget()
        self.stackRandom.setLayout(self.GenerateRandom.StackGenerateRandomNumbersUI())

        # 实例化 BinToString 类
        self.BinToString = BinToString()
        # 创建 QWidget 添加 BinToString 实例
        self.StackBinToString = QtWidgets.QWidget()
        self.StackBinToString.setLayout(self.BinToString.BinToStringUI())

        # 实例化 DeleteBlankLine 类
        self.DeleteBlankLine = DeleteBlankLine()
        # 创建 QWidget 添加 DeleteBlankLine 实例
        self.StackDeleteBlankLine = QtWidgets.QWidget()
        self.StackDeleteBlankLine.setLayout(self.DeleteBlankLine.DeleteBlankLineUI())

        self.StringToBin = StringToBin()
        self.StackStringToBin = QtWidgets.QWidget()
        self.StackStringToBin.setLayout(self.StringToBin.BinToStringUI())


        # 左侧列表和右侧列表中增加元素
        self.leftlist.insertItem(0, "string数据转换为bin")
        self.RightStack.insertWidget(0, self.StackStringToBin)

        self.leftlist.addItem("获得随机数")
        self.RightStack.addWidget(self.stackRandom)
        
        self.leftlist.addItem("bin转换为str数据")
        self.RightStack.addWidget(self.StackBinToString)

        self.leftlist.addItem("删除空白行")
        self.RightStack.addWidget(self.StackDeleteBlankLine)
        

        # 把左侧和右侧列表添加到 HBoxLayout 
        self.HBox = QtWidgets.QHBoxLayout(self)
        # self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        # self.splitter.addWidget(self.leftlist)
        # self.splitter.addWidget(self.RightStack)
        # self.splitter.setStretchFactor(0, 1)
        # self.splitter.setStretchFactor(1, 4)
        # self.HBox.addWidget(self.splitter)
        
        self.HBox.addWidget(self.leftlist)
        self.HBox.addWidget(self.RightStack)
        self.HBox.setStretchFactor(self.leftlist, 1)
        self.HBox.setStretchFactor(self.RightStack, 4)
        self.setLayout(self.HBox)
        

    def display(self, i):
        print("当前索引：", i)
        self.RightStack.setCurrentIndex(i)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    hammer = Hammer()
    hammer.initUI()
    hammer.show()
    sys.exit(app.exec_())
