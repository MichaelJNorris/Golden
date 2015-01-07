# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 18:59:59 2014

@author: michaelnorris
"""

import math
import numpy as np
from fractions import Fraction
import time
import matplotlib.pyplot as plt

# R = Fraction(math.sqrt(2))

def continued(N,D):
    #F = Fraction(R)
    #(N,D) = (F.numerator,F.denominator)
    if N < D:
        N,D = D,N
    L = list()
    print("init: N=",N, ", D=",D)
    while D > 1:
        time.sleep(1)
        #E = int(N/D+0.4999999)
        E = int(N/D)
        L.append(E)
        D,N = abs(N - E*D),D
        print("E=",E," N=",N, ", D=",D)
    if D > 0:
        L.append(N)
    return L
    
def ratio_fit(F,D):
    N = int(F*D+0.5)
    E = abs(F*D - N)*2
    return([Fraction(N,D),E])
    
def ratio_fit_bias(F,D):
    """
    there is an expectation that a large denominator is less good
    than a small one - so it would be good to build in a factor that
    takes into account that as the demoninator gets bigger, the
    numerator has "more chances" to land on a close ratio.
    I'd like to capture that 355/113 is a good approx to pi, but
    239/169 is not such a special approx to sqrt(2).
    From there it would be interesting to map out bad fitting reals - 
    is sqrt(2) the worst fitting number to an integer ratio?
    """
    N = int(F*D+0.5)
    #E = abs(F*D - N)*sum([1/x for x in range(1,D+1)])
    E = abs(F*D - N)*math.sqrt(D)
    return([Fraction(N,D),E])

def ratio_plot(F,Dmax):
    P = [ratio_fit(F,d)[1] for d in range(1,Dmax)]
    plt.plot(P)
    plt.show()

def ratio_best(F,Dmax):
    P = [ratio_fit(F,d) for d in range(1,Dmax)]
    return min(P, key = lambda x: x[1])
    
def ratio_best_bias(F,Dmax):
    P = [ratio_fit_bias(F,d) for d in range(1,Dmax)]
    return min(P, key = lambda x: x[1])
    
def ratio_best_gen(F,Dmax):
    best_err = 2
    for D in range(1,Dmax):
        (R,err) = ratio_fit(F,D)
        if err < best_err:
            best_err = err
            yield (R,err)
            
def ratio_best_plot(F,Dmax):
    """
    interesting that the log error plots for successive best approximations
    of square roots seem to be linear, whereas other irrationals such as pi
    and logs make wiggly lines. I wonder what is behind that... could it be
    related to their simple continued fraction representations?
    """
    L =  list(ratio_best_gen(F,Dmax))
    eps = 1e-50
    plt.plot([math.log(x[1]+eps) for x in L])
    plt.show()
    
# ratio_best(math.pi,20000)
# ratio_best_bias(math.pi,20000)
# tmp=[print(x) for x in list(ratio_best_gen(math.pi,10000))]