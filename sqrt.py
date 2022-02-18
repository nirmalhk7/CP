# 914
# Status: Done

import math

def check(x):

    bin_x= str(bin(x))[2:]
    min_amt= 2**math.floor(((len(bin_x))/2)-1)
    i=0

    while (min_amt+i)**2<=x:
        i+=1
    
    return min_amt+i-1, min_amt, i

print(check(int(input())))