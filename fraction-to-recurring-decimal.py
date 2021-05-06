# 468
# Status: Completed

def soln(N,D):
    neg = True
    if (N < 0 and D < 0) or (N >= 0 and D >= 0): 
        neg = False
    N = abs(N)
    D = abs(D)
    rem = N % D
    q = N // D
    res = [("-" if neg else "") + str(q)]                
    maps = {}        
    if rem == 0:
        return str((-1 if neg else 1) * q)
    else:
        res.append('.')
        while rem != 0:        
            if rem in maps:
                res.append(')')
                res.insert(maps[rem] , '(')
                break;
            else:
                maps[rem] = len(res)
                rem *= 10
                res.append(str(rem // D))
                rem %= D
    return "".join(res)
    


print(soln(1,2))
print(soln(2,1))
print(soln(2,3))
print(soln(4,333))
print(soln(1,5))