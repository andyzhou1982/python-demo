import time

# 定义一个装饰器函数
def sayLocal(func):
    def wrapper():
        curTime = func()
        return f'当地时间： {curTime}'
    return wrapper

@sayLocal
def getXXXTime():
    return time.strftime('%Y_%m_%d %H:%M:%S',time.localtime())

# 装饰 getXXXTime 等价于在getXXXTime函数前加@sayLocal
#getXXXTime = sayLocal(getXXXTime)

print (getXXXTime())  