print(abs)
def add(x,y,f):
    return f(x) + f(y)

f = abs
print(add(5,-6,f))

# ========== map/reduce ===============
def f(x):
    return  x*x
r = map(f,[1,2,3,4])
print(list(r))

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add2(x,y):
    return x+y
print(reduce(add2,[1,3,5,7,9]))
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn,map(char2num,'123456')))

# 整理
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

# lambda简化
def char2num(s):
    return DIGITS[s]
def str2int_2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# =================== filter ===================
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['a','b','','d',None,' '])))

# ==================== sorted =================
print(sorted([1,6,3,5,9,2,1,-4]))
print(sorted([1,6,3,5,9,2,1,-4],key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))

# ==================== return function ===========
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

# ======== 闭包 ===========
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())  #返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量

def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count2()
print(f1(),f2(),f3())

# ========================== lambda ==========================
def f(x):
    return x*x
f = lambda x: x*x
print(f)
print(f(5))

# ========================== decorator =========================
def now():
    print('2015-01-03')

f = now
print(f)
print(f.__name__)

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2015-01-03')

now()   # @log == (now = log(now))

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-01-03')

now()
print(now.__name__)

import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2015-01-03')

now()
print(now.__name__)

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-01-03')

now()
print(now.__name__)

# =============== partial function ==================
print(int('12345'))
print(int('12345',base=8))
print(int('12345',base=16))
int2 = functools.partial(int,base=2)
print(int2('1000000'))