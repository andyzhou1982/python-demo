# 异常对象，代表电话号码有非法字符
class InvalidCharError(Exception):
    pass

# 异常对象，代表电话号码非中国号码
class NotChinaTelError(Exception):
    pass

def register():
    tel = input('请注册您的电话号码:')

    # 如果有非数字字符
    if not tel.isdigit(): 
        raise InvalidCharError()

    # 如果不是以86开头，则不是中国号码
    if not tel.startswith('86'): 
        raise NotChinaTelError()
    
    return tel

try:
    ret = register()
except InvalidCharError:
    print('电话号码中有错误的字符')
except NotChinaTelError:
    print('非中国手机号码')