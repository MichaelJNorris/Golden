# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 15:12:08 2014

@author: michaelnorris
"""

from math import sqrt
import numbers
from fractions import Fraction
import operator

class Golden(Fraction):
    """
    Class implementing extended numbers of the form A*phi+B,
    where A,B are rational, and phi is the Golden Ratio.
    This set is closed under +,-,*,/, and is equivalent to
    the algebraic number field Q(√5).
    Implemented for investigating musical scales such as
    Heinz Bohlen's 833cent scale.
    Also useful for calculations involving fibonacci numbers.
    """
    
    __slots__ = ('_phis', '_ones')    
    
    def __new__(cls, phis=0, ones=0):
        
        self = super(Golden, cls).__new__(cls)
        
        if isinstance(phis,numbers.Rational):
            self._phis = Fraction(phis)
        else: 
            raise TypeError("arguments should be Rational")
            
        if isinstance(ones,numbers.Rational):
            self._ones = Fraction(ones)
        else:
            raise TypeError("arguments should be Rational")
            
        return self
            
    def __repr__(self):
        return ('Golden(%s, %s)' % (self._phis, self._ones))
        
    def __str__(self):
        if self._phis == 0:
            return str(self._ones)
        elif self._ones == 0:
            if self._phis == 1:
                return '\U0001D6DF'
            else:
                return '%s\U0001D6DF' % self._phis 
        else:
            if self._phis == 1:
                return '(\U0001D6DF + %s)' % (self._ones)
            else:
                return '(%s\U0001D6DF + %s)' % (self._phis, self._ones)
   
    def __float__(self):
        phi = (1+sqrt(5))/2
        return float(self._ones)+phi*float(self._phis)  
        
    def __hash__(self):
        return float(self).__hash__()
      
    def _operator_fallbacks(monomorphic_operator, fallback_operator):
        """
        adapted from fractions.Fraction
        """
        def forward(a, b):
            if isinstance(b, (int, Fraction, Golden)):
                return monomorphic_operator(a, b)
            else:
                return NotImplemented
        forward.__name__ = '__' + fallback_operator.__name__ + '__'
        forward.__doc__ = monomorphic_operator.__doc__

        def reverse(b, a):
            if isinstance(a, numbers.Rational):
                # Includes ints.
                return monomorphic_operator(a, b)
            else:
                return NotImplemented
        reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
        reverse.__doc__ = monomorphic_operator.__doc__

        return forward, reverse

    def _add(a, b):
        """a + b"""
        if isinstance(a,Golden):
            if isinstance(b,Golden):
                return Golden( a._phis + b._phis, a._ones + b._ones)
            elif isinstance(b, numbers.Rational):
                return Golden(a._phis, a._ones + b)
        elif isinstance(b,Golden):
            if isinstance(a, numbers.Rational):
                return Golden( b._phis, a + b._ones)
        return NotImplemented
    __add__, __radd__ = _operator_fallbacks(_add, operator.add)

    def _sub(a, b):
        """a - b"""
        if isinstance(a,Golden):
            if isinstance(b,Golden):
                return Golden( a._phis - b._phis, a._ones - b._ones)
            elif isinstance(b, numbers.Rational):
                return Golden(a._phis, a._ones - b)
        elif isinstance(b,Golden):
            if isinstance(a, numbers.Rational):
                return Golden(b._phis, a - b._ones)
        return NotImplemented
    __sub__, __rsub__ = _operator_fallbacks(_sub, operator.sub)

    def _mul(a, b):
        """a * b"""
        if isinstance(a,Golden):
            if isinstance(b,Golden):
                ones = (a._ones * b._ones) + (a._phis * b._phis)
                phis =    (a._ones * b._phis) \
                        + (a._phis * b._ones) \
                        + (a._phis * b._phis)
                return Golden(phis, ones)
            elif isinstance(b, numbers.Rational):
                return Golden(a._phis * b, a._ones * b)
        elif isinstance(b,Golden):
            if isinstance(a, numbers.Rational):
                return Golden(a * b._phis, a * b._ones)
        return NotImplemented
    __mul__, __rmul__ = _operator_fallbacks(_mul, operator.mul)

    def _eq(a, b):
        """a == b"""
        if isinstance(a,Golden):
            if isinstance(b,Golden):
                return (a._ones == b._ones) & (a._phis == b._phis)
            elif isinstance(b, numbers.Rational):
                return (a._ones == b) & (a._phis == 0)
        elif isinstance(b,Golden):
            if isinstance(a, numbers.Rational):
                return (b._ones == a) & (b._phis == 0)
        return NotImplemented
    __eq__, __req__ = _operator_fallbacks(_eq, operator.eq)

    def _gt(a, b):
        """a > b"""
        return float(a) > float(b)
    __gt__, __rgt__ = _operator_fallbacks(_gt, operator.gt)
    
    def _lt(a, b):
        """a < b"""
        return float(a) < float(b)
    __lt__, __rlt__ = _operator_fallbacks(_lt, operator.lt)

    def invert(a):
        denom =    (a._ones * a._ones) \
                + (a._ones * a._phis) \
                - (a._phis * a._phis)
        ones =    (a._ones + a._phis) / denom
        phis =    (- a._phis) / denom
        return Golden(phis, ones)
                
    def _truediv(a, b):
        """a / b"""
        if isinstance(a,Golden):
            if isinstance(b,Golden):
                return a * b.invert()
            elif isinstance(b, numbers.Rational):
                if b != 0:
                    return Golden(a._phis / b, a._ones / b)
        elif isinstance(b,Golden):
            if isinstance(a, numbers.Rational):
                return a * b.invert()
        return NotImplemented
    __truediv__, __rtruediv__ = _operator_fallbacks(_truediv, operator.truediv)
     
    def __abs__(a):
        if float(a) < 0:
            return Golden( -a._phis, -a._ones)
        else:
            return a
       
    def __neg__(a):
        return Golden( -a._phis, -a._ones)

    def __pow__(a,N):
        """
        Would be nice to make a non-recursive version.
        Can't construct non-integer powers.
        """
        if isinstance(N,int):
            if N == 0:
                return Golden(0,1)
            elif N > 0:
                return (a * a.__pow__(N-1))
            else: # negative power
                return Golden(0,1)/a.__pow__(abs(N))

phi = Golden(1)
