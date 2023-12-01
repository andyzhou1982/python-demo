#执⾏字符串表⽰的代码
s1 = "print('helloworld')"
s2 = "2+3"
exec(s1)  #exec执行一段python代码
a = eval(s2) #eval执行表达式并返回表达式的结果
print(f"a={a}")