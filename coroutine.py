def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)


#======================== asyncio ========================
import asyncio
@asyncio.coroutine
def hello():
    print('Hello World!')
    r = yield from asyncio.sleep(1)
    print("Hello again!")
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

#======================== 2 coroutine======================
import threading

@asyncio.coroutine
def hello2():
    print("Hello world! (%s)" % threading.currentThread)
    yield from asyncio.sleep(1)
    print("Hello again! (%s)" % threading.currentThread)

# loop2 = asyncio.get_event_loop()
# tasks = [hello2(),hello2()]
# loop2.run_until_complete(asyncio.wait(tasks))
# loop2.close()

