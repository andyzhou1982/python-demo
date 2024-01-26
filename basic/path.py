import os
import sys


def getCwdPath():
    return os.getcwd()

def getProjectPath():
    current_root_path = os.path.dirname(os.path.dirname(__file__))
    return current_root_path

def getCurrentFilePath():
    return os.path.abspath(__file__)

def getFilePath(file):
    return os.path.abspath(file)

def getSpecialFilePath():
    return os.path.abspath('C:/Users/Administrator/Desktop'+'/resources/numpy.txt')

print(f"currentFilePath:{getCurrentFilePath()}")
print(f"projectPath:{getProjectPath()}")
print(f"cwdPath:{getCwdPath()}")
print(f"filePath:{getFilePath('resources/numpy.txt')}")
print(f"specialFilePath:{getSpecialFilePath()}")

