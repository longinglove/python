def nop():
    pass

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type');
    if x >= 0:
        return x
    else:
        return -x

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s*x
    return s

def enroll(name, gender, age = 6, city = 'BeiJing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

def add_end(L=[]):
    L.append('END')
    return L

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    return sum

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

nop()
print my_abs(1)
print power(5, 3)
print power(10)
enroll('longing', 'M')
enroll('xzz', 'F')
L = [1,2,3]
M = []
print add_end(L)
print add_end(M)
print calc(1,2,3)
print calc(1,2,3,4)
person('Michael', 30)
person('longing', 24, city = 'xi\'an')
func(1,2)
func(1,2,c=3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=99)
