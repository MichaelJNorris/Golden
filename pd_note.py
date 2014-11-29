# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 15:12:08 2014

@author: michaelnorris
"""
from golden import *
import numpy as np
from fractions import Fraction
#import matplotlib.pyplot as plt

def pd_phi_note(ratios,notes_per_phi):
    outfile = open('phi_note.pd','w')
    outfile.write(\
'''#N canvas 561 144 547 262 10;
#X obj 60 -166 inlet n;
#X obj 71 57 outlet note;
#N canvas 0 22 450 278 (subpatch) 0;
#X array \$0-scale 20 float 3;'''+'\n')

#A 0 1 1.09286 1.35715 1.52857 1.75715 1.88572 2 2 2 2 2 2 2 2 2 2 2 2 2 2;
    L = np.arange(0,20)*0.0 + 2.0
    L[:len(ratios)] = [float(x) for x in ratios]
    outfile.write('#A 0 '+ \
            ' '.join([str(round(x,6))for x in L])+';\n')
    
    outfile.write(\
'''#X coords 0 2 20 1 200 140 1 0 0;
#X restore 285 -109 graph;
#X obj 158 -47 tabread \$0-scale;'''+'\n')

#X obj 158 -72 % 7;
    outfile.write('#X obj 158 -72 % '+str(int(notes_per_phi))+';\n')

    outfile.write(\
'''#X obj 60 -142 t f f;
#X obj 39 -47 expr (1+sqrt(5))/2;
#X obj 39 -70 loadbang;'''+'\n')

#X obj 24 -94 div 7;
    outfile.write('#X obj 24 -94 div '+str(int(notes_per_phi))+';\n')

    outfile.write(\
'''#X obj 24 -16 expr pow($f2 \, $f1);
#X obj 71 32 *;
#X connect 0 0 5 0;
#X connect 3 0 10 1;
#X connect 4 0 3 0;
#X connect 5 0 8 0;
#X connect 5 1 4 0;
#X connect 6 0 9 1;
#X connect 7 0 6 0;
#X connect 8 0 9 0;
#X connect 9 0 10 0;
#X connect 10 0 1 0;'''+'\n')

BP_ratios = [BP_note(n) for n in range(-21,21)] # 7 notes per phi

phint6_ratios = [phint6_note(n) for n in range(-24,24)] # 6 notes per phi

       