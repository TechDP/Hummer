# from struct import *
import binascii
import struct


def ModifyFileContent(filename, srcOffset, destOffset, size):
    i = 0
    file = open(filename, "rb+")

    while i < size:
        file.seek(srcOffset+i)      
        data = file.read(1)

        file.seek(destOffset+i)
        file.write(data)

        if not data:
            break

        i += 1

    file.close()


def EraseFileContent(filename, offset, size):
    i = 0
    bytes = struct.pack('B', 0xFF)

    file = open(filename, "rb+")
    file.seek(offset)

    while i < size:
        file.write(bytes)
        i += 1

    file.close()


def CopyFileContent(srcFileName, srcOffset, destFileName, destOffset, size):
    i = 0

    srcFile = open(srcFileName, "rb")
    srcFile.seek(srcOffset)

    destFile = open(destFileName, "rb+")
    destFile.seek(destOffset)

    while i < size:
        data = srcFile.read(1)
        destFile.write(data)

        if not data:
            break

        i += 1

    srcFile.close()
    destFile.close()


def printFileContent(filename, start, end):
    i = 0
    file = open(filename, "rb")
    file.seek(start)

    while i < (end-start):
        data = file.read(1)
        char = str(binascii.b2a_hex(data))[2:-1]

        if (i % 16 == 0) and (i != 0):
            print(end='\n')

        print(char,  end=' ')

        if not data:
            break

        i += 1

    file.close()

if __name__ == "__main__":
    print("********************** Menu **********************")
    print("1: 剪切固件头至0xF1000")
    print("2: 剪切固件头至0xF1000, 0xF0000写入RSA明文数据")
    print("3: 剪切固件头至0xF1000, 0xF0000写入RSA密文数据")
    print("******************** Menu End ********************")

    sel = int(input("please input your choice："))
    if 1 == sel:
        ModifyFileContent("flashBoot.bin", 0, 0xF1000, 0x1000)
        EraseFileContent("flashBoot.bin", 0, 0x1000)
    elif 2 == sel:
        ModifyFileContent("flashBoot.bin", 0, 0xF1000, 0x1000)
        EraseFileContent("flashBoot.bin", 0, 0x1000)
        CopyFileContent("PlainRSA.bin", 0xF0000, "flashBoot.bin", 0xF0000, 0x1000)
    elif 3 == sel:
        ModifyFileContent("flashBoot.bin", 0, 0xF1000, 0x1000)
        EraseFileContent("flashBoot.bin", 0, 0x1000)
        CopyFileContent("CipherRSA.bin", 0xF0000, "flashBoot.bin", 0xF0000, 0x1000)
    elif 4 == sel:
        CopyFileContent("data.bin", 0xE0000, "flashBoot_CiperHasRSA_V4.bin", 0xE0000, 0x10000)  
    else:
        print("无效选项")

    print("Success!")   