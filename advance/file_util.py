import os,shutil
import sys
# 获取上上级目录并添加到path中，之后才可以import basic.file.create_file
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#获取当前工作目录并添加到path中，之后才可以import basic.file.create_file
sys.path.append(os.getcwd())

from basic.file import create_file

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f'创建目录:{path}')

def del_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)

def copy_file(src,dst):
    shutil.copyfile(src,dst)

def copy_dir(src,dst):
    if not os.path.exists(dst):
        shutil.copytree(src,dst)  

def path_exists(path):
    return os.path.exists(path)

def rename_dir(src,dst):
    os.rename(src,dst) 

def rename_file(src,dst):
    os.rename(src,dst)    

def is_file(path):
    return os.path.isfile(path)

def is_dir(path):
    return os.path.isdir(path)

def current_workspace():
    return os.getcwd()

#遍历目录下所有文件
def walk_dir(path):
    for root,dirs,files in os.walk(path):   #不是一次取出所有文件，而是一层一层取出
        for file in files:
            print(f"file path:{os.path.join(root,file)}")
        for dir in dirs:
            print(f"dir path:{os.path.join(root,dir)}")


create_dir('resources/bak')
create_file('resources/bak/test.txt')
copy_file('resources/doc.txt','resources/bak/bak.txt')
copy_dir('resources/bak','resources/bak1')
del_dir('resources/bak')
del_dir('resources/bak2')
rename_dir('resources/bak1','resources/bak2')
rename_file('resources/bak2/bak.txt','resources/bak2/bak2.txt')
print(f"目录resources/bak1是否存在:{path_exists('resources/bak1')}")
print(f"resources/bak2是否为目录:{is_dir('resources/bak2')}")
print(f"resources/bak2/bak2.txt是否为文件:{is_file('resources/bak2/bak2.txt')}")
print(f"当前工作目录:{current_workspace()}")
walk_dir('resources')
