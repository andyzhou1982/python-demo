
#用lambda表达式进行过滤
def filterList(l):
    print(f"l.type={type(l)}")
    a = filter(lambda x: x>10,l)
    print(f"a.type={type(a)}")
    b = list(a)
    print(f"b.type={type(b)}")
    return b

l = [1,11,2,45,7,6,13]
print(f"fil={filterList(l)}")