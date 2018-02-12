#coding: utf-8

import time
import datetime
import numpy as np

def getDateTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

def getTime():
    return datetime.datetime.now()


#梯度下降求根号N
def desc_sqrt(N):
    x=1
    for i in range(50000):
        x=x-0.0001*(x**2-N)
        # print x
    print "近似值：",x
    print "真实值：",np.sqrt(N)
    return x


def desc_pow(pow):
    x=1
    for i in range(100000):
        x=x-0.0001*(1/x-pow)
    print "近似值：",x
    print "真实值：",np.exp(pow)
    return x



class Fibonacci:
    tmp = 0

    def __init__(self):
        pass

    # 尾递归
    def fib(self, n, a, b):
        if (n < 2):
            return a
        return self.fib(n - 1, b, a + b)

    # 带缓存的递归
    def fibmy(self, n):
        if (n < 2):
            self.tmp = n
            return self.tmp, n
        tup = self.fibmy(n - 1)
        print tup
        self.tmp = tup[1]
        return self.tmp, self.tmp + tup[0]


if __name__ == '__main__':
    fibb = Fibonacci()
    # print fibb.fib(7, 1, 1)
    print fibb.fibmy(7)