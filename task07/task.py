import time
tick = time.time()
print(tick)

localtime = time.localtime(time.time())
print(localtime)

t = time.localtime()
print("本地时间为：%s" %time.asctime(t))

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S:%Y",time.localtime()))



class Ticket:
    def __init__(self,workday=True,adult=True):
        self.price=100
        if workday:
            self.ratio=1
        else:
            self.ratio=1.2
        if adult:
            self.discount=1
        else:
            self.discount=0.5

    def get_price(self,num):
        return self.price*self.ratio*self.discount*num

adult_1=Ticket(workday=True,adult=True)
child_1=Ticket(workday=True,adult=False)

print("2个成人+1个小孩平日票价为：%.2f" %(adult_1.get_price(2)+child_1.get_price(1)))
