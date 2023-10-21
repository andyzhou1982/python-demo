import datetime
import time

def get_time1():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())


def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def get_year():
    return datetime.datetime.now().year


print(type(time.time())==float)
print(f"time={time.time()}")
print(f"localtime={time.localtime()}")
print(f"get_year={get_year()}")
print(f"get_time1={get_time1()}")
print(f"get_time={get_time()}")