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
