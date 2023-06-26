import time
from datetime import datetime

def get_timestamp():
    return int(time.time())

#获得毫秒级的时间戳
def get_timestamp_ms():
    return int(time.time()*1000)

def get_time():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

def get_time1():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    #return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time))

def get_timestamp_from_str(time_str):
    return int(time.mktime(time.strptime(time_str,'%Y-%m-%d %H:%M:%S')))    

print(f"当前时间戳是：{get_timestamp()}")
print(f"获取毫秒级别的时间戳：{get_timestamp_ms()}")
print(f"当前时间是：{get_time1()}")
print(f"将时间2020-06-09 06:00:00转化为时间戳是：{get_timestamp_from_str('2020-06-09 06:00:00')}")

