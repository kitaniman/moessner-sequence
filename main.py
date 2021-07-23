from MoessnerSequence import *

def f(x):
    return 2*x

def tri(x):
 return int((x+1)*x/2)

s = MoessnerSequence(7, tri)

print(s)