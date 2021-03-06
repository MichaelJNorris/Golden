# Golden

Musings on the mathematics of musical tunings. Includes a python type Golden to manipulate numbers of the form (A𝛟 +B ), and Python code that calculates musical tuning frequencies and makes them available to PureData patches.

## golden.py
Defines an immutable type based on Fraction.

Golden(A,B) represents the number (A𝛟 +B) where A and B are rational (of type Fraction) and 𝛟 is the Golden Ratio: 𝛟=(1+sqrt(5))/2. The resulting number system is equivalent to Q(√5), the field of rationals extended by the irrational √5. This set is closed under addition, subtraction, multiplication and division. These four basic operations are defined for all combinations of Golden and Rational (including Fraction and int). Operations also defined include float, abs, unary minus and raising to an integer power.

This python class was originally written for exploring the properties of inharmonic musical scales based on difference tones, such as the Bohlen-Pierce scale, and led to an alternative experimental musical scale “Phint6”. It has also proved useful for simplifying calculations involving the fibonacci series.

## test_golden.py
Test script for the Golden type.

## fibonacci.py
A simple non-recursive fibonacci function, plus some functions for exploring Zeckendorf sets.

## continued.py
Continued fractions and other rational approximations.

## tunings.py
A variety of musical tunings including Equal Temperament, Just Intonation, Bohlen-Pierce and others that have come out of my own explorations. Also includes code to write tuning frequencies to a PureData object for use in synthesis.

## tuning_properties.py
A few measures of how well a tuning fits various criteria.

# PureData

##tuning_* 
These objects have been generated by the python code in tunings.py.

## ztest_tuning.pd
An example of how to use the tuning objects. Makes simple chords.

## ztest_instr.pd
An example of how to drive a simple instrument. No nice instruments to be found here yet. In particular, instr_synth.pd is not a great instrument. Need to make something better.

## ztest_chord.pd
Generative patch using chords and arpeggios in various tunings. Uses an instrument built around ring modulating sine waves. Not terribly musical yet.