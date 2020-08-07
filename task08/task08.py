import datetime
dt = datetime.datetime(year=2020,month=8,day=7,hour=17,minute=12,second=23)
print(dt)
print(dt.timestamp())
dt = datetime.datetime.fromtimestamp(1596791543.0)
print(dt)
print(type(dt))
dt = datetime.datetime.now()
print(dt)
print(type(dt))

dt = datetime.datetime(year=2020, month=6, day=25, hour=11, minute=51, second=49)
s  = dt.strftime("'%Y/%m/%d %H:%M:%S")
print(s)
s = dt.strftime('%d %B ,%Y ,%A')
print(s)

d = datetime.date.today()
print(d)
print(type(d))

d1 = datetime.date(1869, 1, 2)
d2 = datetime.date(1869, 10, 2)
dt  = (d2 -d1).days
print(dt)
print(d1.isoweekday())
print(dt // 7 + 1)