# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 15:12:08 2014

@author: michaelnorris
"""
from golden import Golden
import numpy as np
import matplotlib.pyplot as plt

"""
NEWER CODE THAT PRODUCED PHINT8
"""

def insert_element(S,E):
    if E > 0:
        D = [max(E,x)/min(E,x) for x in S if x>0]
        if float(min(D)) > 2**(1/20): # less than 1/2 semitone
            S.add(E)
    return S

def extend_set(S):
    New = set(S)
    for A in S:
        for B in S:
            if A > B:
               New = insert_element(New,(abs(A-B)))
               New = insert_element(New,(abs(2*A-B))) 
               New = insert_element(New,(abs(A-2*B)))
    return New

def scale_golden_free():
    """
    This is what Phint8 was based on
    """
    S = set({Golden(1,0),Golden(0,1)})
    S = extend_set(S)
    S = extend_set(S)
    S = extend_set(S)
    F = F = [500*float(x) for x in S]
    F.sort()
    return (S,F)
    
def plot_set(S):
    F = [float(x) for x in S]
    F.sort()
    plt.plot(F)
    plt.show()

"""
OLDER CODE THAT PRODUCED PHINT6
"""
    
def messiness(M):
    '''
    Something to minimise
    '''
    return abs(M._ones.numerator) \
        + 2*abs(M._ones.denominator) \
        + 4*abs(M._phis.numerator) \
        + 8*abs(M._phis.denominator)
        
def ratio(A,B):
    if A > B:
        if B > 0:
            return A/B
        else:
            return 0
    else:
        return ratio(B,A)
        
def more_than_semitone(a,b):
    fa = float(a)
    fb = float(b)
    return max(fa,fb)/min(fa,fb) > 1.06 # 1.06 => 6 note scale
    
def phint_scale():
    """
    start with [1,phi] and repeatedly:
    - generate all sums & differences
    - exclude those <1/12 or >12
    = exclude those too close to an existing note (< semitone)
    - generate all ratios between existing & candidate notes
    - order by simplest
    - one at a time:
        -insert if ratio with nearest existing note < semitone
    until none inserted
    """
    Lnotes = [Golden(0,1),Golden(1,0)]
    Done = False
    while not Done:
        Done = True
        Lcandidates = []
        fnotes = [float(x) for x in Lnotes]
        for d in set([x+y for x in Lnotes for y in Lnotes] + \
                [abs(x-y) for x in Lnotes for y in Lnotes]):
            fd = float(d)
            if (fd>0.1) & (fd<10):
                if all([more_than_semitone(fd,fn) for fn in fnotes]):
                    Lcandidates.append(d)
        
        if len(Lcandidates) > 0:
            ## really want least messy diffs with all existing notes        
            mess = lambda M: sum([messiness(ratio(M,x)) \
                        for x in Lcandidates])
            Lcandidates.sort(key=mess)
            for d in Lcandidates:
                if all([more_than_semitone(d,x) for x in Lnotes]):
                    Lnotes.append(d)
                    Done = False
    Lnotes.sort(key=float)
    return Lnotes
    
