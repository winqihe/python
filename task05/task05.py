i = 1
print(id(i))
i = i+2
print(id(i))

x = [1,2]
print(id(x))
x.append('python')
print(id(x))

print(hash('name'))
print(hash((1,2,'xiaohe')))

'''列表，集合，字典是可变类型，不能被hash
print(hash([1,2,'xiaoming']))
print(hash({1,2,'xiaoming'}))
'''
dic = {'清华':'北京','复旦':'上海','川大':'成都'}
print('复旦在:',dic['复旦'])

dic = dict()
dic['a']=1
dic['b']=2
dic['c']=3
print(dic)
dic['a']=99
print(dic)
dic['d']= 434
print(dic)

dic1 = dict([('apple',123),('banana',213),('yus',345)])
print(dic1)
dic2 = dict((('iphone',7899),('sanxing',3444),('huawei',2333)))
print(dic2)
dic3 = dict(name='xiaoxiao',age = 19)
print(dic3)
print(type(dic3))

seq = {'name','age','sex'}
dic1 = dict.fromkeys(seq)
print(dic1)
dic2 = dict.fromkeys(seq,10)
print(dic2)
dic3 = dict.fromkeys(seq,('小文',20,'男'))
print(dic3)

dic = {'name': 'xiaoming', 'age':19}
print(dic.keys())
lst = list(dic.keys())
print(lst)

dic = {'name': 'xiaoming', 'age':19}
print(dic.values())
lst = list(dic.values())
print(lst)
dic = {'name': 'xiaoming', 'age':19}
print(dic.items)
lst = list(dic.items())
print(lst) 
dic = {'name': 'xiaoming', 'age':19}
print(dic.get('name'))

dic = {'name': 'xiaoming', 'age':19}
if 'name' in dic:
    print('name存在')
else:
    print('name不存在')
if 'sex' not in dic:
    print('sex不存在')
else:
    print('sex存在')

dic = {'name': 'xiaoming', 'age':19}
print(dic.pop('name'))

dic = {'name': 'xiaoming', 'age':19}
del dic['name']
print(dic)
dic = {'name': 'xiaoming', 'age':19}
print('长度为:',len(dic))
dic.clear()
print('长度为：',len(dic))
dic = {'name': 'xiaoming', 'age':19}
dic1 ={}
print(dic1)
dic1 = dic.copy()
print(dic1)

dic1 = {'name': 'xiaoming', 'age':19}
dic2 = dic1
dic3 = dic1.copy()
print(id(dic1))
print(id(dic2))
print(id(dic3))
dic1 = {'name': 'xiaoming', 'age':19}
dic2 = {'name': 'xiaohe', 'age':34}
dic1.update(dic2)
print(dic1)

dic = {
    'python': 95,
    'java': 99,
    'c': 100
    }
print(len(dic))
dic2 = {'java':98}
dic.update(dic2)
print(dic)
dic.pop('c')
print(dic)
dic3= {'php':90}
dic.update(dic3)
print(dic)
dic1 = list(dic.keys())
print(dic1,type(dic1))
dic4 =list(dic.values())
print(dic4,type(dic4))

if 'javascript' in dic:
    print("javascript存在")
else:
    print("JavaScript不存在")
print(sum(dic.values()))
print(max(dic.values()))
print(min(dic.values()))
dic1 = {'php':97}
dic.update(dic1)
print(dic)