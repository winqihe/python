a = 'xiaoming'
print(a,type(a))
b = '5'+'8'
print(b,type(b))
print('let\'s go ')
print('aaa\nbbb')
print('aaa\rbbb')

str1= 'i love xiao ming'
print(str1[:6])
print(str1[5])
print(str1[2:4])

a= 'python'
print(a[-1])
print(a[4])

b = 'dota'
print(b.capitalize())
print(b.upper())
print(b.swapcase())
print(b.lower())

a = 'aaadota'
print(a.count('a'))
print(a.startswith('aaad'))
print(a.endswith('ta'))
print(a.find('do'))
print(a.rfind('do'))
print(a.find('od'))

b = '1234'
print(b.isnumeric())
c = 'dota'
d = b +c
print(d.isnumeric())

a = 'xiaoming'
print(a.strip().replace('xiao','lao'))

u = "www.baidu.com.cn"
print(u.split())
print(u.split('.'))
print(u.split('.',0))
print(u.split('.',1))
print(u.split('.',2))
print(u.split('.',2)[1])
print(u.split('.',2)[2])
u1,u2,u3 = u.split('.',2)
print(u1)
print(u2)
print(u3)
c = '''say
hello
baby'''
print(c)
print(c.split('\n'))
