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

#����������ʱ������ִ���κ����������������䣬��������yield���ʽ��һ�л���һ��
#next()��send(None)����ʼִ�е�yield�й���yield��ֵ����next()
#send(value) ��next()��value����yield�Ⱥ���ߣ�yield��һ�е����˳��ִ��
#����һ��ִ��send()��next(),����ִ�е�yield��һ��

