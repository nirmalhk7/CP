# 5633
# Easy Difficulty
# Completed Status.

def soln(n):
    cumsumhash={1:1,2:3,3:6,4:10,5:15,6:21,7:28}
    def recursive(days,w=0):
        if(days<=7):
            return cumsumhash[days]+days*w
        else:
            return cumsumhash[7]+7*w+recursive(days-7,w+1)
    return recursive(n)

print(soln(4))
print(soln(20))
print(soln(10))