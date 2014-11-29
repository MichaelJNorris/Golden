# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 09:36:05 2014

@author: michaelnorris
"""

from golden import *
from fractions import Fraction
from math import sqrt

def test_golden():
    assert(Golden()==Golden(0,0)) # default is zero
    assert(Golden(1)==Golden(1,0)) # single argument is phis
    assert((Golden(1)*2-1)**2==Golden(0,5)) # identity of phi
    
    A = Golden(Fraction(2,7),Fraction(17,29))
    B = Golden(Fraction(3,11),Fraction(19,31))
    C = Golden(Fraction(5,13),Fraction(23,37))
    
    # Commutative properties
    assert( A+B == B+A )
    assert( A*B == B*A )
    
    # Associative properties
    assert( (A+B)+C == A+(B+C) )
    assert( (A*B)*C == A*(B*C) )
    
    # Distributive properties
    assert( A*(B+C) == A*B + A*C )
    assert( (A+B)/C == A/C + B/C )
    assert( (A*B)**5 == A**5 * B**5)
    assert( A**5 == A**3 * A**2)
    
    # Inverse Properties    
    assert( A-B == -(B-A) )
    assert( A/B == 1/(B/A) )
    assert( ((A+B) - B) == A )
    assert( ((A-B) + B) == A )
    assert( ((A*B) / B) == A )
    assert( ((A/B) * B) == A )