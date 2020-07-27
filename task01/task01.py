#hello,world入门开始
print("hello,world")
# 注释使用#来注释整行，多行注释使用'''来注释。
#运算符:
print(2+1)  #加+
print(2-1)  #减-
print(2*1)  #乘*
print(10/3) #除/
print(10//3)#整除//
print(10%3) #求余%
print(2**4) #幂**
#比较运算符：
print(2 > 1)  # 大于
print(2 >= 4)  # 大于等于
print(1 < 2)  # 小于
print(5 <= 2)  # 小于等于
print(3 == 4)  # 等于
print(3 != 5)  # 不等于
#逻辑运算符：
print((3 > 2) and (3 < 5))  # 与
print((1 > 3) or (9 < 2))  # 或
print(not (2 > 1))  # 非
#三元运算符：
x,y=4,5
small=x if x<y else y
print(small)
'''其他运算符
in：存在
not in 不存在
letters = ['a','b','c']
if 'a' in letters:
    print('a'+"存在")
if 'd' not in letters:
    print('h'+"不存在")
is：是
is not：不是
a = "hello"
b = "hello"
print(a is b,a == b)
print("==========")
print(a is not b,a != b)
is,is not 比较是两个变量的内存地址
运算符的优先级：
一元运算符优于二元运算符，先算术运算，后移位运算，最后位运算，逻辑运算最后结合
'''
#变量和赋值:
#python中变量名可以包括字母，数字，下划线，但不可以数字开头
#python变量名大小写敏感
name="文奇的编程开发学习"
print(name)
a = 2
b = 3
c=a+b
print(c)
name1=",小文的python学习"
name2=name+name1
print(name2)
#数据类型与转换:
# 整形int
a = 3
print(a,type(a))
print(4,type(4))
#浮点型float
print(2,type(2.))
a = 0.0000003
print(a)
b= 3e-07
print(b)
#布尔型boolean
#可以使用bool(x)来创建变量，x可以是基本类型，也可以是容器类型
print(True+True)
print(True+False)
print(False+False)
#作用在基本类型变量，X 只要不是整型 0、浮点型 0.0，bool(X) 就是 True，其余是 False
print(type(0),bool(0),bool(1))
print(type(2.31),bool(0.00),bool(2.31))
print(type(True),bool(False),bool(True))
#作用在容器类型变量，bool 作用在容器类型变量：X 只要不是空的变量，bool(X) 就是 True，其余是 False
print(type(''),bool(''),bool('python'))
print(type(()),bool(()),bool((10,)))
print(type([]),bool([]),bool([1,2]))
print(type({}),bool({}),bool({'a':1,'b':2}))
print(type(set()),bool(set()),bool({1,2}))
#获取类型信息
#type(object)
print(type(2))
print(type('hello'))
print(type(3.2))
print(type(False))
#isinstance(object,classinfo)
print(isinstance(1,int))
#判断两个类型是否相等使用isinstance()
'''类型转换:
转换为整型 int(x, base=10)
转换为字符串 str(object='')
转换为浮点型 float(x)'''
print(int(521))
print(int(521.520))
print(float('521.23'))
print(float(521))
print(str(10+10))
print(str(19.4+2.3))
#print函数：
print(*objects,sep='',end='\n',file=sys.stdout,flush=False)
'''
将对象以字符串表示的方式格式化输出流文件对象file里
关键字参数sep是实现分隔符
关键字参数end是输出结束时的字符，默认是\n
关键字参数file是定义流输出的文件
关键字参数flush是立即把内容输出到流文件，不做缓存
'''
list = ['java','python','c++','R']
print("This is printed with 'end='&''.")
for item in list:
    print(item)

list = ['java', 'python', 'R', 'c++']
print("This is printed with 'sep='&''.")
for item in list:
    print(item, 'another string', sep='&')

'''位运算
原码：二进制表示
反码：正数的反码就是原码，负数的反码就是符号位不变，其余为取反。
补码：正数的补码就是原码，负数的补码是反码+1。
'''
#位非操作：~ 把num的补码中的 0 和 1 全部取反（0 变为 1，1 变为 0）有符号整数的符号位在 ~ 运算中同样会取反。
#位与操作：&只有两个对应位都为 1 时才为 1
#位或操作：|只要两个对应位中有一个 1 时就为 1
#位异或操作：^只有两个对应位不同时才为 1,满足交换律和结合律
5 ^0 #=5
1 ^1 #=0
1 ^0 #=1
#位左移操作<< num << i 将num的二进制表示向左移动i位所得的值。
#位右移操作>> num >> i 将num的二进制表示向右移动i位所得的值。
