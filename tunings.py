# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 15:12:08 2014

@author: michaelnorris
"""

from golden import *
from fibonacci import *
from fractions import Fraction
import matplotlib.pyplot as plt

def tuning_frequencies(note_fn,freq_mult,min_freq,max_freq):
    freq = lambda x: float(note_fn(x))*freq_mult
    min_ind = 40
    while freq(min_ind+1) < min_freq: # go above lowest note
        min_ind += 4
    while freq(min_ind-1) > min_freq: # come back down to lowest note
        min_ind -= 1
    max_ind = min_ind + 1
    while freq(max_ind+1) < max_freq: # find highest note
        max_ind += 1
    return [freq(x) for x in range(min_ind,max_ind+1)]

def pd_read_only_array(patch_name,array_data):
    outfile = open(patch_name+'.pd','w')
    outfile.write(\
'''#N canvas 160 170 1100 380 10;
#X obj 40 30 loadbang;
#X msg 40 50 ''' + \
    " \, ".join([str(x) for x in array_data]) + \
''';
#X obj 40 260 write_ro_array;
#X obj 40 280 outlet array_spec;
#X connect 0 0 1 0;
#X connect 1 0 2 0;
#X connect 2 0 3 0;'''+'\n')

def write_tunings_to_pd():
    pd_write = lambda pd_name, py_fn, freq_mult : \
        pd_read_only_array(pd_name,tuning_frequencies(py_fn,freq_mult,27,4200))
    pd_write("tuning_Equal",Equal_note,440)
    pd_write("tuning_Just",Just_note,440)
    pd_write("tuning_Just_MN",Just_MN_note,440)
    pd_write("tuning_Fib8",Fib8_note,1)
    pd_write("tuning_BP",BP_note,440)
    pd_write("tuning_Phint6",Phint6_note,440)
    pd_write("tuning_Phint8",Phint8_note,440)
        
def Equal_note(N):
    """
    12-note per octave Equal Temperament scale
    """
    return 2**(N/12)

def BP_note(N):
    """
    Bohlen-Pierce scale ratios
    """
    BP_ratios = [Golden(0, 1),
                 Golden(Fraction(1,2),Fraction(1,4)),
                 Golden(-3, 6),
                 Golden(2, -2),
                 Golden(Fraction(1,2),Fraction(1,2)),
                 Golden(Fraction(2,3),Fraction(1,3)),
                 Golden(-4, 8)
                 ]
    return BP_ratios[N%7]*(phi**(N//7))
    
def Phint6_note(N):
    """
    6-note per phi scale on int*phi+int
    Interesting scale for pure tone synthesis and ring modulation.
    Has more sums and differences within scale than Bohlen-Pierce,
    though fewer integer ratios, so sounds pleasantly musical if only
    within-scale frequencies are used, but gets very noisy if any
    harmonics are added.
    """
    ratios = [Golden(0, 1),\
        Golden(26, -41), \
        Golden(-3, 6), \
        Golden(2, -2), \
        Golden(-1, 3), \
        Golden(4, -5)]
    return ratios[N%6]*(phi**(N//6))

def Phint8_note(N):
    """
    8-note per phi scale on int*phi+int
    Fairly close to semitones.
    """
    ratios = [Golden(0, 1), \
        Golden(5, -7), \
        Golden(-3, 6), \
        Golden(2, -2), \
        Golden(-6, 11), \
        Golden(-1, 3), \
        Golden(4, -5), \
        Golden(9, -13), \
        Golden(1, 0)]  
    return ratios[N%8]*(phi**(N//8))

def Just_MN_note(N):
    """
    12-note custom Just scale.
    """
    ratios = [Fraction(1, 1), \
             Fraction(11, 10), \
             Fraction(6, 5), \
             Fraction(5, 4), \
             Fraction(4, 3), \
             Fraction(7, 5), \
             Fraction(3, 2), \
             Fraction(8, 5), \
             Fraction(5, 3), \
             Fraction(7, 4), \
             Fraction(9, 5), \
             Fraction(19, 10)]
    return ratios[N%12]*(Fraction(2)**(N//12))
    
def Just_note(N):
    """
    12-note Just scale
    """
    ratios = [Fraction(1, 1), \
             Fraction(16, 15), \
             Fraction(9, 8), \
             Fraction(6, 5), \
             Fraction(5, 4), \
             Fraction(4, 3), \
             Fraction(7, 5), \
             Fraction(3, 2), \
             Fraction(8, 5), \
             Fraction(5, 3), \
             Fraction(9, 5), \
             Fraction(15, 8)]
    return ratios[N%12]*(Fraction(2)**(N//12))
    
def Fib8_note(N):
    """
    7-note per phi Fibonacci scale - lowest note is zero, returns Hz
    Pattern of intervals effectively repeats from every 8th note, but
    generated from integer Hz values, so not exact repetition.
    """
    K = (N//8)+9
    B = [int(x) for x in list('{0:0b}'.format(8+N%8))][1:]
    return fibonacci(K) + \
            B[0]*fibonacci(K-3) + \
            B[1]*fibonacci(K-5 + B[0]) + \
            B[2]*fibonacci(K-7 + B[0] + B[1]) 
            
def Fib16_note(N):
    """
    15-note per phi Fibonacci scale - lowest note is zero, returns Hz
    """
    K = (N//16)+17
    B = [int(x) for x in list('{0:0b}'.format(16+N%16))][1:]
    return fibonacci(K) + \
            B[0]*fibonacci(K-3) + \
            B[1]*fibonacci(K-5 + B[0]) + \
            B[2]*fibonacci(K-7 + B[0] + B[1]) + \
            B[3]*fibonacci(K-9 + B[0] + B[1] + B[2]) 