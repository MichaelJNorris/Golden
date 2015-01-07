# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 10:20:09 2015

@author: michaelnorris
"""
from golden import *
from tunings import *
from fractions import Fraction
import matplotlib.pyplot as plt
from continued import ratio_best
    
def in_scale(S,E):
    if E == 0:
        return False
    D = [max(E,x)/min(E,x) for x in S if x>0]
    return min(D) < 2**(1/120) # 1/10 semitone
    
def percent_in_scale_harmonic(L):
    Nin = Nout = 0
    for A in L:
        for B in L:
            if A > B:
               if in_scale(L,abs(A-B)) \
               and in_scale(L,abs(2*A-B)) \
               and in_scale(L,abs(A-2*B)):
                   Nin += 1
               else:
                   Nout += 1
    return 100*Nin/(Nin+Nout)
    
def percent_in_scale_diff(L):
    Nin = Nout = 0
    for A in L:
        for B in L:
            if A > B:
               if in_scale(L,abs(A-B)):
                   Nin += 1
               else:
                   Nout += 1
    return 100*Nin/(Nin+Nout)
    
def ratio_err(L):
    count = err = 0
    for A in L:
        for B in L:
            if A > B:
                count += 1
                err += ratio_best(float(A/B),100)[1]
    return 100*err/count
    
def ratio_denom(L):
    count = denom = 0
    for A in L:
        for B in L:
            if A > B:
                count += 1
                denom += ratio_best(float(A/B),1000)[0].denominator
    return 0.1*denom/count
    
def scale_report(L):
    count = err = Nin = denom = 0
    for A in L:
        for B in L:
            if A > B:
                count += 1
                if in_scale(L,abs(A-B)):
                    Nin += 1
                R = ratio_best(float(A/B),100)
                err += R[1]
                denom += R[0].denominator

    print("Percent pairs with diff in scale: ", 100*Nin/count)
    print("Mean best denom of pair ratios: ", denom/count)
    print("Mean % error from best ratio for pairs: ", 100*err/count)
                
def cents(L):
    R = [y/L[x] for x,y in enumerate(L[1:])]
    C = [1200*log2(x) for x in R]
    return [int(x+0.5) for x in C]
    
L = tuning_frequencies(Equal_note,440,27,4200) 
L = tuning_frequencies(Just_note,440,27,4200) 
L = tuning_frequencies(Just_MN_note,440,27,4200) 
L = tuning_frequencies(Phint6_note,440,27,4200) 
L = tuning_frequencies(Phint8_note,440,27,4200) 
L = tuning_frequencies(Fib8_note,1,27,4200)  
L = tuning_frequencies(Fib16_note,1,27,4200)  
                
def cents(L):
    R = [y/L[x] for x,y in enumerate(L[1:])]
    C = [1200*log2(x) for x in R]
    return [int(x+0.5) for x in C]
    
    
    
    
    
    