import traceback

def level_3():
    print ('进入 level_3')
    try:
        a = [0]
        b = a[1]
    except :
        print(f'未知异常:{traceback.format_exc()}')
    print ('离开 level_3')

def level_2():
    print ('进入 level_2')
    level_3()
    print ('离开 level_2')

def level_1():
    print ('进入 level_1')
    level_2()
    print ('离开 level_1')


level_1()

print('程序正常退出')