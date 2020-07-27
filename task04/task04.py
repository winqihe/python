#列表
x = ['xiaoming','xiaowang','xiaofang']
print(x,type(x))
y = [1,2,3,4,5]
print(y,type(y))

x = list(range(10))
print(x,type(x))

y = list(range(1,20,3))
print(y,type(y))

x = list(range(10,2,-2))
print(x, type(x))

x = [0]*5
print(x,type(x))

y = [0 for i in range(10)]
print(y,type(y))

x = [i for i in range(10)]
print(x,type(x))
 
y = [i for i in range(1,10,2)]
print(y,type(y))

x = [i**2 for i in range(1,10)] 
print(x,type(x))

y = [i for i in range(100) if (i % 2) ==0 and(i% 3)==0]
print(y,type(y))

x= [[1,2,3],[4,5,6],[7,8,9],[0,0,0]]
print(x,type(x))
for i in x :
    print(i,type(i))
y = [1,'xiaoming',[1,2,3],2.34]
print(y,type(y))
empty = []
print(empty)
x = ['xiaoming','xiaowang','xiaofang','xiaoli']
x.append('xiaohe')
x.append(['xiaodu','xiaohang'])
for i in x:
    print(i)
print(len(x))

y =[1,2,3,4,5]
print(y)
y.extend([6,7,8,9])
print(y)
print(len(y))

x = [11,22,33,44,55]
print(x)
x.insert(2,25)
print(x)
x.remove(44)
print(x)
y = x.pop(1)
print(y)

x = [1,2,3,4]
y = x.pop(-2)
print(y)

x = [1,2,3,4,5]
del x[0:3]
print(x)

x = ['xiaolizi','xiaowang','xiaohe','xiaohei']
print(x[0],type(x[0]))
print(x[-2],type(x[-2]))
print(x[2:])
print(x[-1:])
print(x[:1])
print(x[:-2])
print(x[1:2])
print(x[-3:-1])

y = [1,2,3,4,5,6]
print(y[1:4:2])
print(y[::-1]) #相当于将列表反向
print(y[:])

x = [1,4,5,6,3,7,8]
x.sort
print(x[:])

list1 = [123, 456]
list2 = [456, 123]
list3 = [123, 456]
print(list1 == list2)
print(list1 == list3)

list4 = list1+ list2
print(list4)

list5 = list3 *3
print(list5) 
print(123 in list3)
print(456 not in list3)

x = [1,3,4,5,4,5,6,4,3,3,4]
print(x.count(3))
print(x.count(4))

x = [12,33,44,55,65]
x.reverse()
print(x)
x.sort()
print(x)
