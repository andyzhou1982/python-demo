#encode字符串
def encode(s):
    return s.encode('utf-8')   #将字符串转换成bytes类型
#decode字符串
def decode(s):
    return s.decode('utf-8')

input_str = '你好'
output_str = encode(input_str)
print(f"对字符串{input_str}进行编码:{output_str}")
print(f"对字符串{output_str}进行解码:{decode(output_str)}")