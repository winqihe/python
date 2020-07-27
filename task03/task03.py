import random
a = random.randint(0,100)
b = 1
c = 0
while b:
    c+=1
    guess = int(input("请输入一个位于1-100间的数字:"))
    if isinstance(guess,int):
        pass
    else:
        print("输入无效")
    if guess > a:
        print('猜的大了')
    elif guess <a:
        print('猜的小了')
    else:
        print("你猜对了,很厉害嘛")
        break
