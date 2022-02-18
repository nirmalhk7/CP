# 507
# Status: Found from GFG

import math
def list_divisors(num):
    divlist=[]
    for i in range(1,math.ceil(math.sqrt(num))):
        if(num%i==0):
            divlist.append(int(i))
            if(i!=1):
                divlist.append(int(num/i))
        # print(divlist)
    return divlist

def fun(x):
    return list_divisors(x)

print(fun(int(input())))