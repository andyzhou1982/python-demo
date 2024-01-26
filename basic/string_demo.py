import codecs


def convert_newlines(s):
    return s.encode().decode()

def another_function(param):
    # 这里是你想在这个函数中做的操作
    print(param)

original_string = '你好\\n世界'
converted_string = convert_newlines(original_string)

another_function(converted_string)