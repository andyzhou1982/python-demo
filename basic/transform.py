#整形转浮点型
def int_to_float(x):
    return float(x)
#浮点型转整形
def float_to_int(x):
    return int(x)
#浮点型转字符串
def float_to_str(x):
    return str(x)
#字符串转浮点型
def str_to_float(x):
    return float(x)

a = int_to_float(10)
b = float_to_int(10)
print("a的值为%s,b的值为%s"%(a,b))
print(f"a的值为{a},b的值为{b}")