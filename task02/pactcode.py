'''
a =1
while a ==1:
    num = int(input("输入一个数字："))
    print("你输入的数字为：",num)
print("goodbye")
b=int(input("请输入一个数字；"))
while b<8:
    print(b,"b小于等于8")
    b=b+1
else: 
    print(b,"b大于或等于8")

a =1
while(a):print("hello")
print("byebye")

a ="start"
for x in a:
    print(x)
food=["apple","banana","pool","..."]
for x in food:
    print(x)

name=["xiaoming","xiaofang","xiaohei","xiaoqiang","xiaowang"]
for xname in name:
    if xname=="xiaofang":
        print(xname,"是一个女孩子")
        break
else:
        print(xname,"是个糙汉子")
print("gameover")

for x in range(13):
    print(x)
for x in range(5,9):
    print(x)
for x in range(0,21,3):
    print(x)
for x in range(-10,-30,-10):
    print(x)

a= ["xiaohei","liulang","tf","longying"]
for x in range(len(a)):
    print(x,a[x])

print(list(range(3,19,3)))

goods = ["girlfriends","woman"]
for x in goods:
    if x == "man":
        print("this is a man")
        break
else:
    print("this is a girl")

for letter in 'Python':     # 第一个实例
   if letter == 'h':
      break
   print ('当前字母 :',letter)

var =10
while var >0:
    print('当前变量值',var)
    var = var-1
    if var ==6:
        break
print("bye")

for letter in "Python":
    if letter == 'h':
        continue
    print('当前字符：',letter)

var = 10                   
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print('当前变量值 :', var)
print("Good bye!")

for letter in 'Python':
    if  letter == 'h':
        pass
        print("this is a pass")
    print("当前字母：",letter)
print("byebye")

count =0 
while count < 3:
    temp = input("可以猜一下我现在想的是哪个数字：")
    guess = int(temp)
    if guess > 8:
        print("大了大了")
    else:
        if guess ==8:
            print("哈哈哈哈，你现在想的是什么呢?")
            print("猜对了，你挺厉害呢吗")
        else:
            print("小了小了")
    count = count + 1
print("游戏结束，拜拜了")
'''
#?
'''
string = "abcd"
while string:
    print(string)
    string=string[1:]

count = 0
while count <5:
    print("python厉害吗")
    count = count +1
else:
    print("java天下第一")

count = 0
while count < 5:
    print("java天下第一")
    count = 8
    break
else:
    print("python可能也不错吧")

for i in 'ILOVEYOU':
    print(i,end='')

num =["张三","成龙","贺文奇","马云"]
for each in num:
    print(each)
for i in range(len(num)):
    print(num[i])

dic ={'a':1,'b':2,'c':3,'d':4}
for key,value in dic.items():
    print(key,value,sep=':',end=' ')

dic ={'a':1,'b':2,'c':3,'d':4}
for key in dic.keys():
    print(key,end=' ')

dic ={'a':1,'b':2,'c':3,'d':4}
for value in dic.values():
    print(value,end=' ')

for num in range(10,20):
    for i in range(2,num):
        if num % i ==0:
            j = num /i 
            print('%d 等于 %d * %d' % (num, i, j))
            break
    else:
        print(num,'是一个质数')

for i in range(1,6):
    print(i)

for i in range(1,20,3):
    print(i)

lan = ['java','python','R',"linux"]
lists = list(enumerate(lan))
print(lists)
lan = ['java','python','R',"linux"]
lists = list(enumerate(lan,2))
print(lists)

language = ['java','python','javascript','R']
for languages in language:
    print('I Love',languages)
print('Do it Now')
language = ['java','python','javascript','R']
for i,languages in enumerate(language,5):
    print(i,'I Love',languages)
print('do it now')

x=[2,-3,1,5]
y=[a*2 for a in x]
print(y)

a=[x*2.5 for x in range(1,5)]
print(a)

a= [x**4 for x in range(1,3)]
print(a)

x = [(i,i**2) for i in range(6)]
print(x)

x= [i for i in range(100) if (i%2)!=0 and (i%3)==0]
print(x)

x = [(i,j) for i in range(1,3) for j in range(0,3)]
print(x)

x = [[i,j] for i in range(1,3) for j in range(0,3)]
print(x)
x[0][0] = 10
print(x)

x = [(i,j) for i in range(0,3) if i <1 for j in range(0,3) if j>1]
print(x)

a = (x for x in range(10))
print(a)
print(tuple(a))

x = {i:i % 2 == 0 for i in range(10) if i % 3==0 }
print(x)

x = {i for i in {1,2,3,3,4,5,2,1}}
print(x)
d = 'i for i in "i love python"'
print(d)

c = (i for i in range(10))
print(c)
print(next(c))
print(next(c))
print(next(c))
for each in c :
    print(each,end=' ')

s =sum([i for i in range(101)])
print(s)
s= sum((i for i in range(101)))
print(s)

x = [i for i in range(1500,2700) if (i %7)==0 and (i % 5)==0]
print(x)
'''