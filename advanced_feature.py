# -*- coding: utf-8 -*-

# ============ List comprehension ============
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

# ============ Generator =====================
L = [x * x for x in range(10)]
G = (x * x for x in range(10))
print(L)
print(G)
for n in G:
    print(n)

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        # print(b)
        yield b   # generator 遇到yield返回，下次在返回处继续执行
        a,b = b,a+b
        n = n + 1
    return 'done'
# print(fib(6))
# f = fib(6)
# print(f)
for n in fib(6):
    print(n)
def odd():
    print('step1')
    yield 1
    print('step2')
    yield 3
    print('step3')
    yield 5

o = odd()
print(next(o))
next(o)
next(o)