import time

class Mytime (object):
    def __init__(self):
        self.__info = '未开始计时'
        self.__begin = None
        self.__end = None
        self.__jg =0
    def __str__(self):
        return self.__info
    def __repr__(self):
        return self.__info
    def start(self):
        print('计时开始...')
        self.__begin = time.localtime()
    def stop(self):
        if not self.__begin:
            print('请先进行计时...')
            return
        self.__end = time.localtime()
        self.__jg = time.mktime(self.__end) - time.mktime(self.__begin)
        self.__info = '共运行了%d秒'% self.__jg
        print('计时结束')
        return self.__jg
    def __add__(self,other):
        return '共运行了%d秒' % (other.__jg + self.__jg)
t1 = Mytime()
print(t1)
t1.stop()
t1.start()
time.sleep(6)
t1.stop()
print(t1)
t2 = Mytime()
t2.start()
time.sleep(4)
t2.stop()
print(t2)
print(t1+t2)