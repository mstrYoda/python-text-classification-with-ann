import numpy as np


def sigmoid(x):
    output = 1 / (1 + np.exp(-x))
    return output

def carpma(a,b,c,d):
    return (a*b) + (c*d)

def s(c,e):
    return c*(1-c)*e

def agirlikHesapla():
    pass

#print sigmoid()

#print carpma()

#print s()

