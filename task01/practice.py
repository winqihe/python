practice
1：可以使用#对单行代码进行注释，对于多行代码注释可以使用'''注释内容'''进行注释
2：算术运算符，逻辑运算符，比较运算符，位运算符，三元运算符，in，not in，is，is not，
运算符优先级：
一元运算符<二元运算符
逻辑运算<移位运算<算术运算
3：is is not和== ！=的区别是is，is not比较的是两个变量的内存地址，而==，！=比较的是两个变量的值
4：数据类型int，float，bool这类数据类型
转换为整形：int(x,base=10)
转换为字符串：str(object='')
转换为浮点型：float(x)
5：leetcode练习题
example1 = [4,1,2,1,2]
b = 0
for i in example1:
    b ^= i
print(b)
example 2 =[1,2,2]
c = 0
for i in example2:
    c ^= i
print(c)