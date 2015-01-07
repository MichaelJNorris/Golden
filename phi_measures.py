# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 09:28:46 2014

@author: michaelnorris
"""

def diff_table(scale,note_numbers):
    '''
    produces dictionaries mapping pairs of note numbers to sums
    and differences where those are in the scale
    scale is a mapping from note number to ratio
    '''
    scale_dict = {}
    for N in note_numbers: # build reverse mapping
        scale_dict[scale(N)] = N
    sums = {}
    diffs = {}
    for a in note_numbers:
        for b in note_numbers:
            if a < b:
                # sums
                combin = scale(a) + scale(b)
                if combin in scale_dict.keys():
                    sums[(a,b)] = scale_dict[combin]
                # diffs
                combin = abs(scale(a) - scale(b))
                if combin in scale_dict.keys():
                    diffs[(a,b)] = scale_dict[combin]
    return (sums,diffs)

def harmonic_table(scale,note_numbers):
    '''
    produces a dictionary mapping pairs of note numbers that
    are harmonically related to their ratio
    scale is a mapping from note number to ratio
    '''
    harmonic = {}
    for a in note_numbers:
        for b in note_numbers:
            if a > b:
                ratio = scale(a) / scale(b)
                if ratio._phis == 0: # no irrational component
                    harmonic[(a,b)] = ratio._ones
    return harmonic

def octaves(scale,note_numbers):
    '''
    produces a dictionary mapping pairs of note numbers that
    are harmonically related to their ratio
    scale is a mapping from note number to ratio
    '''
    oct = set()
    for a in note_numbers:
        for b in note_numbers:
            if scale(b) == (2*scale(a)):
                oct.add((a,b))
    return oct

"""
# Bohlen-Pierce
BD = diff_table(BP_note,range(-20,21))
BH = harmonic_table(BP_note,range(-20,21))

# Phint6
PD = diff_table(Phint6_note,range(-20,21))
PH = harmonic_table(Phint6_note,range(-20,21))
"""

"""
The Phint6 scale has many more in-scale sums and difference than
the Bohlen-Pierce scale, but fewer harmonicly related notes.
"""
def dict_to_tuple(D):
    Lsets = [set.union(set(k),set([D[k]])) for k in D]
    Ltuple = [tuple(sorted(list(x))) for x in Lsets]
    return Ltuple

def triples(SD,N):
    # SD is sums and differences from diff_table
    # N is notes per phi, so 7 for BP, 6 for phint6
    S = set(dict_to_tuple(SD[0]))
    S.union(set(dict_to_tuple(SD[1])))
    Snew = set()
    for T in S:
        if T[-1]-T[0] < 3*N:
            shift = N*(T[0]//N)
            if len(T) == 3:
                Snew.add((T[0]-shift,T[1]-shift,T[2]-shift))
            else: # double
                Snew.add((T[0]-shift,T[1]-shift))
    return Snew
    
#BT = triples(BD,7)
#PT = triples(PD,6)
        