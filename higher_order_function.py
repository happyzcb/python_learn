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
