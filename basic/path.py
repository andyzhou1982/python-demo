import os

def getProjectPath():
    return os.path.abspath('.')

def getProjectPath1():
    return os.getcwd()

def getCurrentFilePath():
    return os.path.abspath(__file__)

def getFilePath(file):
    return os.path.abspath(file)

def getSpecialFilePath():
    return os.path.abspath('C:/Users/Administrator/Desktop'+'/resources/numpy.txt')

print(f"currentFilePath:{getCurrentFilePath()}")
print(f"projectPath:{getProjectPath()}")
print(f"projectPath1:{getProjectPath1()}")
print(f"filePath:{getFilePath('resources/numpy.txt')}")
print(f"specialFilePath:{getSpecialFilePath()}")

