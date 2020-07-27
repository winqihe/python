#if语句
if 2 > 1 and 3>2:
    print("这是正确的啊")
#if-else语句
temp =input("猜猜我现在在干嘛呢")
guess=str(temp)
if guess == "敲代码":
    print("回来正确的了哦")
    print("要不要一起来听首歌")
else :
    print("你猜错了哦")
print("不玩了，敲代码去了")

hello =3
if hello > 2:
    print("厉害厉害")
else:
    print("这都不明白吗？")
#if语句嵌套：
temp = input("猜猜我的幸运数字是多少啊")
guess = int(temp)
if guess >8:
    print("大了哦，")
else:
    if guess==8:
        print("猜对了，好棒")
    else:
        print("小了小了")
print("游戏结束，回家吃饭吧")
#if-elif-else语句:
#elif即为else-if语句
temp=input("账户余额！")
source=int(temp)
if 1000>source>900:
    print('A')
elif 900>source>800:
    print('B')
elif 800>source>600:
    print('C')
elif 600>source>0:
    print('D')    
else :
    print("账户余额不足！")
#assert关键字
'''assert断言，当关键字后面的条件为False，程序自动崩溃并抛出AssertionError异常'''
assert 5>8
