# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 15:12:08 2014

@author: michaelnorris
"""
import numpy as np
import matplotlib.pyplot as plt


def fib(F,N):
    for i in range(N):
        F.append(F[-1]+F[-2])
    return F

def sums(S):
    out = set()
    for A in S:
        for B in S:
            out.add(A+B)
    return out.difference(S)

def diffs(S):
    out = set()
    for A in S:
        for B in S:
            if max(A,B)/min(A,B) < 4.3:
                out.add(abs(A-B))
    out.discard(0)
    return out.difference(S)
    
phi = (1+np.sqrt(5))/2

def make_diff_scale():
    D = set([4400/phi,4400])
    while min(D) > 60:
        D = diffs(D).union(D)
    return D

D = make_diff_scale()

L = np.sort(np.array(list(D)))
