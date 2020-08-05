class Animal:
    def run(self):
        raise AttributeError('子类必须实现这个方法')
class People(Animal):
    def run(self):
        print('人正在走')
class Pig(Animal):
    def run(self):
        print('pig is walking')
class Dog(Animal):
    def run(self):
        print('dog is running')
def func(animal):
    animal.run()
func(Pig())
func(Dog())

class Tur:
    def climb(self):
        print("climb in")
    def run(self):
        print("run in ")
    def eat(self):
        print("eat in")
    def sleep(self):
        print("sleep in")
tt =  Tur()
tt.eat()
tt.climb()

class MyList(list):
    pass
lst = MyList([1,2,3,4,5,6,7,8])
lst.append(9)
lst.sort
print(list(lst))

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
tt= Test()
tt.prt()

class Ball:
    def setname(self,name):
        self.name= name
    def kick(self):
        print("我是%s，该死的，谁踢我..."% self.name)
a = Ball()
a.setname("小明")
b = Ball()
b.setname("小王")
a.kick()
b.kick()

class Ball:
    def __init__(self,name):
        self.name = name
    def kick(self):
        print("我是%s，该死的，谁踢我..."% self.name)
a=Ball("xi")
b=Ball("sb")
c=Ball("二狗")
a.kick()
b.kick()
c.kick()

class Tur:
    def __init__(self,x):
        self.num= x
class Fish:
    def __init__(self,x):
        self.num = x
class Pool:
    def __init__(self,x,y):
        self.tur = Tur(x)
        self.fish = Fish(y)
    def printnum(self):
        print("水池里面的乌龟有%s只，小鱼有%s条"% (self.tur.num,self.fish.num))
p = Pool(2,3)
p.printnum()

class C :
    def setX(self,x,y):
        self.x = x
        self.y = y
    def printXY(self):
        print(self.x,self.y)
dd = C()
dd.setX(2,3)
dd.printXY()
print(dd.__dict__)
print(vars(dd))

class C:
    def myFun(self):
        print('Hello!')
c = C()
c.myFun()