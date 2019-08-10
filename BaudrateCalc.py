SYSCTRL_Frequency_ALL = [54]
PLL_DIV_ALL = [1]
HCLK_DIV_ALL = [4]
PCLK_DIV_ALL = [2]

USED_Baudrate = [110, 300, 600, 1200, 2400, 4800, 9600, 1440, 19200, 38400, 56000, 57600, 115200, 128000, 230400, 256000, 460800, 500000, 512000, 600000, 750000, 912600, 1000000]

def IS_BaudrateCanUse(PCLK_Frequency, Baudrate):
    tmpBaudRateDiv = int(((PCLK_Frequency / 16) + Baudrate / 2) / Baudrate)
    if tmpBaudRateDiv == 0:
        return 0
    RealBaudrate = PCLK_Frequency / (tmpBaudRateDiv * 16)
    if abs(Baudrate - RealBaudrate) < Baudrate * 0.05:
        return 1
    else:
        return 0

CanUsedBaud = []
UniversalBaud = set(USED_Baudrate)
for SYS_Freq in SYSCTRL_Frequency_ALL:
    for PLL_DIV in PLL_DIV_ALL:
        if SYS_Freq == 12:
            PLL_DIV = 1
        for HCLK_DIV in HCLK_DIV_ALL:
            # 1903的限制
            if SYS_Freq / PLL_DIV > 102:
                HCLK_DIV = 2
            for PCLK_DIV in PCLK_DIV_ALL:
                for Baudrate in USED_Baudrate:
                    PCLK_Frequency = SYS_Freq * 1000000 / PLL_DIV / HCLK_DIV / PCLK_DIV
                    if IS_BaudrateCanUse(PCLK_Frequency, Baudrate) == 1:
                        CanUsedBaud.append(Baudrate)
                print("SYS_Freq: ", SYS_Freq)
                print("PLL_DIV: ", PLL_DIV, "CPU_Freq: ", SYS_Freq / PLL_DIV)
                print("HCLK_DIV: ", HCLK_DIV, "HCLK_Freq: ", SYS_Freq / PLL_DIV / HCLK_DIV)
                print("PCLK_DIV: ", PCLK_DIV, "PCLK_Freq: ", SYS_Freq / PLL_DIV / HCLK_DIV / PCLK_DIV)
                print(list(CanUsedBaud))
                UniversalBaud = set(CanUsedBaud) & UniversalBaud
                CanUsedBaud = []

print("所有分频都通用的波特率：", UniversalBaud)
print("所有分频都通用的最大波特率：", max(UniversalBaud))
    

import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class BaudrateCalc(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.resize(600, 400)
        self.setWindowTitle("BaudrateCalc")
        self.BaudrateCalcUI()
    
    def BaudrateCalcUI(self):
        return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = BaudrateCalc()
    test.initUI()
    test.show()
    sys.exit(app.exec_())
