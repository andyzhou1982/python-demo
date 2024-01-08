def dict_pop(d, key):
    value = d.pop(key)
    return value

def dict_del(d, key):
    del d[key]

#遍历dict
def dict_iter(d):
    for k, v in d.items():
        print(f"key={k},value={v}")

def dict_clear(d):
    d.clear()            

#合并两个字典对象
def dict_merge(d1, d2):
    d1.update(d2)

if __name__ == '__main__':
    d = {'a': 1, 'b': 2, 'c': 3}
    print(dict_pop(d, 'a'))
    print(f"d = {d}")

    d = {'a': 1, 'b': 2, 'c': 3}
    dict_del(d, 'a')
    print(f"d = {d}")

    dict_iter(d)
    dict_clear(d)
    print(f"d = {d}")

    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'d': 4, 'e': 5, 'f': 6}
    dict_merge(d1, d2)
    print(f"d1 = {d1}")