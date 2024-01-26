import io
import json
import codecs
import sys
#print(sys.getdefaultencoding())

def list_to_json(data):
    return json.dumps(data,ensure_ascii=False,indent=4)

def json_to_list(data):
    return json.loads(data)


def str_to_dict(json_str):
    decoder = json.JSONDecoder()
    data = decoder.decode(json_str)
    #print(type(data))
    return data

def format_str(obj):
    #obj = str.encode(obj)
    decoded_string: str = obj.encode().decode()
    #print(decoded_string)
    return decoded_string


historyTransactions = [
    {
        'time'   : '20170101070311',  # 交易时间
        'amount' : '3088',            # 交易金额
        'productid' : '45454455555',  # 货号
        'productname' : 'iphone7'     # 货名
    },
    {
        'time'   : '20170101050311',  # 交易时间
        'amount' : '18',              # 交易金额
        'productid' : '453455772955', # 货号
        'productname' : '奥妙洗衣液'   # 货名
    }
]



# dumps 方法将数据对象序列化为 json格式的字符串
'''
jsonstr = list_to_json(historyTransactions)
print(f"序列化后的json字符串:{jsonstr}")
list = json_to_list(jsonstr)
print(f"反序列化后的list:{list}")
'''
#json_str = '{\\n \\"name\\": \\"John\\", \\"age\\": 30, \\"city\\": \\"New York\\" \\n}'
json_str = '{\\n    \\"question\\": \\"哪些部件是汽车基础改装必须有的？\\",\\n    \\"answer\\": \\"汽车基础改装必须有的部件包括：轮毂和轮胎、避震器（短弹簧、运动套装、绞牙可选）、火花塞（不一定）、动力系统、进排气（排气喉+进气风箱或高流量风格）。\\"\\n}'
#json_str = '{"question": "哪些部件是汽车基础改装必须有的？",    "answer": "汽车基础改装必须有的部件包括：轮毂和轮胎、避震器（短弹簧、运动套装、绞牙可选）、火花塞（不一定）、动力系统、进排气（排气喉+进气风箱或高流量风格）。"}'
json_str = json_str.replace('\\"', '\"')
json_str = json_str.replace('\\n', '\n')
print(format_str(json_str))
#print(str_to_dict(json_str))

'''
a='{"question": "哪些部件是汽车基础改装必须有的？",    "answer": "汽车基础改装必须有的部件包括：轮毂和轮胎、避震器（短弹簧、运动套装、绞牙可选）、火花塞（不一定）、动力系统、进排气（排气喉+进气风箱或高流量风格）。"}'
print(type(a),a,len(a))
a = a.encode('utf-8')
#a = bytes(a,encoding='unicode_escape')
print(type(a),a,len(a))
mid=a.decode("unicode_escape")
print(type(mid),mid,len(mid))
'''

'''
s = '{\\n \\"name\\": \\"John\\", \\"age\\": 30, \\"city\\": \\"New York\\" \\n}'
s = '{\n \"name\": \"吉奥\", \"age\": 30, \"city\": \"纽约\" \n}'
b = b'\xe4\xbd\xa0\xe5\xa5\xbd'
c = b'\\u4f60\\u597d'
print(s.encode('utf-8'))
print(s.encode('unicode_escape'))
print(s.encode('unicode-escape'))
print(s.encode('unicode_escape').decode('unicode_escape'))
print(s.encode().decode())
print(codecs.decode(s.encode()))
'''

'''
a = '\u5403\u9e21\u6218\u573a'
b = a.encode('unicode_escape')
c = b.decode('utf-8')
d = b.decode('unicode_escape')
print(b)
print(c)
print(d)
'''