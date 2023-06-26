import json
def list_to_json(data):
    return json.dumps(data,ensure_ascii=False,indent=4)

def json_to_list(data):
    return json.loads(data)


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
jsonstr = list_to_json(historyTransactions)
print(f"序列化后的json字符串:{jsonstr}")
list = json_to_list(jsonstr)
print(f"反序列化后的list:{list}")