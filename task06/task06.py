def name(str):
    print(str)
name("贺文奇")
def myfirstdef(name):
    "函数定义过程中name是形参"
    print('传递进来的{0}是实参,因为它是具体的参数值'.format(name))
myfirstdef('我在学习java')

print(myfirstdef.__doc__)  
help(myfirstdef)

def printinfo(name, age=8):
    print('Name:{0},Age:{1}'.format(name, age))
printinfo('小文')
printinfo('小文',10)

def printinfo(arg,*arg1):
    print(arg)
    for var in arg1:
        print(var)
print(10)
print(12,23,34)

def printinfo(arg1, *args, **kwargs):
    print(arg1)
    print(args)
    print(kwargs)
printinfo(12,12,34)
printinfo(23,32,45,a=1,b=2)

def add(a,b):
    print(a+b)

add(12,23)

def back():
    return{'xiao':1,'ming':2}
print(back())

def printme(str):
    print(str)
printme('贺文奇最牛逼')

def outer():
    print("这是外层")
    def inner():
        print("这是内层")
    inner()
outer()

def funx(x):
    def funy(y):
        return x*y
    return funy
a = funx(5)
print(type(a))
print(a(3))

def outer():
    num = 10
    def inner():
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)
outer()

n =5
for i in range(1,5):
    n = i * n
    print(n)

def fact(n):
    if n ==1:
        return 1
    return n*fact(n-1)
print(fact(5))
odd = lambda x : x%2==1
temp = filter(odd,[1,2,3,4,5,6,7,8,9])
print(temp)
print(list(temp))