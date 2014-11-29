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
            out.add(abs(A-B))
    out.discard(0)
    return out.difference(S)
    
phi = (1+np.sqrt(5))/2
    
S0 = set([440/phi,440])
S1 = sums(S0).union(diffs(S0)).union(S0)
S2 = sums(S1).union(diffs(S1)).union(S1)
S3 = sums(S2).union(diffs(S2)).union(S2)

L0 = np.sort(np.array(list(S0)))
L1 = np.sort(np.array(list(S1.difference(S0))))
L2 = np.sort(np.array(list(S2.difference(S1))))
L3 = np.sort(np.array(list(S3.difference(S2))))
