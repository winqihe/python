data = list(map(int, input().split()))

v1 = data[0]  # 兔子的速度v1
v2 = data[1] # 乌龟的速度v2
tv1= data[2] # 兔子对应的t
st = data[3] # 兔子对应的s
L = data[4] #赛道的长度l

time = TL = RL =  0

while True:
    if RL - TL >= tv1:
        for i in range(st):
            TL += v2
            time += 1
            if TL >= L > RL:
                print("T")
                print(time)
                exit()
        # RL += 0
    else:
        RL += v1
        TL += v2
        time += 1

    if RL >= L > TL:
        print("R")
        print(time)
        break
    elif TL >= L > RL:
        print("T")
        print(time)
        break
    elif RL == TL >= L:
        print("D")
        print(time)
        break
