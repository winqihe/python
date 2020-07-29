num = {}
num1 = {1,2,3,4,5,6}
print(num,type(num))
print(num1,type(num1))

a = set()
a.add('java')
a.add('php')
a.add('python')
print(a)
b = set('Java')
print(b)
b = set(("Google", "Lsgogroup", "Taobao", "Taobao"))
print(b)  
c = set(['xiaoming','xiaohe','xiaofang'])
print(c)

lst = [0, 1, 2, 3, 4, 5, 5, 3, 1]
temp = []
for item in lst:
    if item not in temp:
        temp.append(item)
print(temp)
a = set(lst)
print(a)

s = set(['Google', 'Baidu', 'Taobao'])
for item in s:
    print(item)
print("xiaoming" in s)
print('Taobao' not in s)
s.remove('Taobao')
s.discard("Taobao")
a = set(['xiaoming','xiaohei','xiaoq'])
a.pop()
print(a)

se = set(range(5))
sw = list(se)
sq = tuple(se)
print(se,type(se))
print(sw,type(sw))
print(sq,type(sq))

a = frozenset(range(5))
print(a,type(a))

a =list()
print(a)

b = 'l love you '
c= list(b)
print(c)

c ='1,2,3,4,5,6,6'
d = list(c)
print(d)

c = [1,2,3,4,5,6,]
d = tuple(c)
print(d)

c = (1,2,3,4,5,6)
d = list(c)
print(d)

a = 123
a = str(a)
print(a,type(a))

c = '123456 '
print(len(c))

print(max(range(5)))

x = [1,5,6,3,4,7]
print(sorted(x))
print(sorted(x,reverse=True))

t = [1,2,3,4,5,6]
x = reversed(t)
print(x,type(x))
print(list(x))

lan = {'java','python','c++','R'}
a = list(enumerate(lan))
print(a,type(a))

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
zipd = zip(a,b)
print(zipd)
print(list(zipd))
zipd = zip(a,c)
print(list(zipd))

a1,a2 = zip(*zip(a,b))
print(list(a1))
print(list(a2))