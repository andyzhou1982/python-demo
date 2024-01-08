def add(a, b, c):
    return a + b + c

# 解包列表为单独的元素s
def unpack():
    numbers: list[int] = [1, 2, 3, 4, 5]
    print(*numbers) 

# 解包列表作为函数参数
def unpackListAsParams():
    values = [1, 2, 3]
    print(add(*values))

# 解包字典作为函数参数
def unpackDictAsParams():
    kwargs = {"a": 1, "b": 2, "c": 3}
    print(add(**kwargs))

def foo(*args, **kwargs):
    print(args)  # 打印位置参数元组
    print(kwargs)  # 打印关键字参数字典

unpack()
unpackListAsParams()
unpackDictAsParams()
foo(1, 2, 3, a=4, b=5)