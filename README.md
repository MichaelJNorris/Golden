# Golden

Python type Golden to manipulate numbers of the form (A𝛟 +B ).

## golden.py
Defines an immutable type based on Fraction.

Golden(A,B) represents the number (A𝛟 +B) where A and B are rational (of type Fraction) and 𝛟 is the golden ratio: 𝛟=(1+sqrt(5))/2. The resulting number system is equaivalent to Q(√5), he field of rationals extended by the irrational √5. This set is closed under addition, subtraction, multiplication and division. These four basic operations are defined for all combinations of Golden and Rational (including Fraction and int). Operations also defined include float, abs, unary minus and raising to an integer power.

This python class was originally written for exploring the properties of inharmonic musical scales based on difference tones, such as the Bohlen-Pierce scale, and led to an alternative experimental musical scale “Phint6”. It has also proved useful for simplifying calculations involving the fibonacci series.

## fibonacci.py
A simple non-recursive fibonacci function, plus some functions for exploring Zeckendorf sets.

## pd_note.py
Writes a PureData patch that implements produces frequencies in a phi-based scale given a note number. Just a utility for experiments - not very smart or general.

