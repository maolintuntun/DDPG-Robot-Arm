# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:51:13 2017

@author: lenovo
"""

MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y
MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print ('The largar one is %d' % MAXIMUM(a,b))
    print ('The lower one is %d' % MINIMUM(a,b))
