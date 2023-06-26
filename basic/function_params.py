studentInfo = {
    '张飞' :  18,
    '赵云' :  17,
    '许褚' :  16,
    '典韦' :  18,
    '关羽' :  19,
}

def  printAge(*students) : #可变参数
    print(type(students))
    for  student in students:
        print( f'学生：{student} , 年龄 {studentInfo[student]}')

printAge('张飞', '典韦', '关羽')

#参数展开
onebatch = ['张飞', '典韦', '关羽']
printAge(*onebatch)