# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 18:18:56 2014

@author: michaelnorris
"""
from math import *
from fractions import gcd
from golden import *

def fibonacci(n):
    """
    non-recursive fibonacci
    """
    phi = (1.0+sqrt(5.0))/2.0
    return round(phi**n/(3-phi))
    
def fib_set(x):
    """
    The set of indices of fibonacci numbers that add to x
    S = fibset(33)
    L = [fib(n) for n in S]
    sum(L)
    result should never contain consecutive indices
    """
    phi = (1.0+sqrt(5.0))/2.0
    S = set()
    while x > 0:
        if x <= 2:
            ind_max_fib = x
        else:
            ind_max_fib = int(log(x*(3-phi),phi))
            if x == fibonacci(ind_max_fib+1): # x was fib
                ind_max_fib += 1
        S.add(ind_max_fib)
        x = x - fibonacci(ind_max_fib)
    return S
    
def zeckendorf(x):
    return set([fibonacci(f) for f in fib_set(x)])
    
def Fib8_note(N):
    """
    8-note per phi Fibonacci scale - lowest note is zero, returns Hz
    """
    K = (N//8)+9
    B = [int(x) for x in list('{0:0b}'.format(8+N%8))][1:]
    return fibonacci(K) + \
            B[0]*fibonacci(K-3) + \
            B[1]*fibonacci(K-5 + B[0]) + \
            B[2]*fibonacci(K-7 + B[0] + B[1]) 
            
def Fib16_note(N):
    """
    16-note per phi Fibonacci scale - lowest note is zero, returns Hz
    """
    K = (N//16)+9
    B = [int(x) for x in list('{0:0b}'.format(16+N%16))][1:]
    return fibonacci(K) + \
            B[0]*fibonacci(K-3) + \
            B[1]*fibonacci(K-5 + B[0]) + \
            B[2]*fibonacci(K-7 + B[0] + B[1]) + \
            B[3]*fibonacci(K-9 + B[0] + B[1] + B[2]) 
            
    