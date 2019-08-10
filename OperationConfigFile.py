#/bin/usr/python3
#-*- coding:utf-8 -*-

import json
import os

class Save(object):
    def __init__(self):
        pass
    
    def ReadConfigFile(self):
        with open("config.json", 'r') as FileRead:
            ConfigData = FileRead.readline()
            if ConfigData:
                return json.loads(ConfigData)
            else:
                return {}

    def WriteConfigFile(self, data):
        

    def GetCWD(self, ModelName):
        if ModelName in self.ReadConfigFile():
            self.cwd = self.ReadConfigFile()[ModelName]
        else:
            self.cwd = os.getcwd()
        return self.cwd

    def WriteConfigFileCWD(self):
        with open("config.json", 'w') as FileWrite:
            tmp = {}
            tmp["BinToStringCWD"] = self.FileNameSelected
            print("write json data:", tmp["BinToStringCWD"])
            FileWrite.write(json.dumps(tmp))

if __name__ == "__main__":
    test = Save()
    print(test.GetCWD('BinToStringCWD'))
    print(test.ReadConfigFile())