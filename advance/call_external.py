import os
from subprocess import Popen

def call_wget_by_os():
    cmd = fr'wget http://nginx.org/download/nginx-1.24.0.zip -OutFile D:\backup\nginx-1.24.0.zip'
    os.system(cmd)
    print('下载完毕')

def call_wget_by_subprocee():
    proc = Popen(
        args='wget http://nginx.org/download/nginx-1.24.0.zip -OutFile D:\backup\nginx-1.24.0.zip',
        shell=True
    )
    print ('让它下载，我们接下来做其他事情。。。。')    

call_wget_by_os()
print('其他代码')