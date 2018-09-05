#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gen():
    for i in range(10):
        print('before yield')
        x = yield i
        #print('x: %s' % x)
        print('after yield: ',x)
        
g = gen()        

#print('get g.send(NOne) value: %s' % g.send(None))
#print('get next(g) value %s' % next(g))
#print('get yeild value %s' % g.send(5))
print(next(g))        
print(next(g))        
print(next(g))        
print(next(g))        

#生成生成器时并不会执行任何生成器函数里的语句，无论是在yield表达式上一行或下一行
#next()或send(None)，则开始执行到yield行挂起，yield的值传到next()
#send(value) 或next()将value传给yield等号左边，yield下一行的语句顺序执行
#即第一次执行send()或next(),不会执行到yield下一行

