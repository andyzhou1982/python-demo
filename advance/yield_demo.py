

def addlist(alist):
    for i in alist:
        yield i + 1

alist = [1, 2, 3, 4]
for x in addlist(alist):
    print(x)      
'''输出 
2 
3 
4 
5
'''


'''
def s():
    print('study yield')
    m = yield 5
    print(m)
    d = yield 16
    print('go on!')

c = s()
s_d1 = next(c)  # 相当于c.send(None)
s_d2 = c.send('Fighting!')  # (yield 5)表达式被赋予了'Fighting!'
print('My Birth Day:', s_d1, '.', s_d2)
'''
#输出My Birth Day: 5 . 16
