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

def sums(S,k):
    out = set()
    for A in S:
        for B in S:           
            if max(A,B)/min(A,B) < k:
                out.add(round(A+B,6))
    return out.difference(S)

def diffs(S,k):
    out = set()
    for A in S:
        for B in S:
            if max(A,B)/min(A,B) < k:
                out.add(round(abs(A-B),6))
    out.discard(0)
    return out.difference(S)
    
phi = (1+np.sqrt(5))/2

def make_sum_scale():
    S = set([44,44*phi])
    while max(S) < 4000:
        S = sums(S,1.5).union(S)
    return S

def make_diff_scale():
    S = set([4400/phi,4400])
    while min(S) > 60:
        S = diffs(S,4.3).union(S)
    return S

def make_sumdiff_scale():
    S = set([440/phi,440])
    while min(S) > 50:
        S = diffs(S,2.01).union(sums(S,2.01)).union(S)
    return S

def make_expand_scale():
    S = set(fib([round(180/phi,6),180],3))
    k = 1.7
    while len(S) < 70:
        #print('len(S)',len(S))
        S = diffs(S,k).union(sums(S,k)).union(S)
    return S

D = make_diff_scale()
S = make_sum_scale()
B = make_sumdiff_scale()
E = make_expand_scale()

LD = np.sort(np.array(list(D)))
LS = np.sort(np.array(list(S)))
LB = np.sort(np.array(list(B)))
LE = np.sort(np.array(list(E)))
LE = LE[(LE>45) & (LE<4000)]




def spine_sums(N):
    Spine = list(np.power(phi,np.arange(0,21)))
    rndsum = lambda x, y: round(x+y,4)
    for iN in range(2,N+2):
        Slist = list(map(rndsum,Spine[iN:],Spine[:-iN]))
        Spine = list(set(Slist).union(set(Spine)))
        Spine.sort()
    Spine = np.array(Spine)
    Spine = Spine[(Spine>45) & (Spine<4000)]
    return Spine