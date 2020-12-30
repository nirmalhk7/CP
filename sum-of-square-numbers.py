# 633
# Medium Difficulty
# Completed Status.

def soln(c):
    def isI(n):
        # print('xx',n)
        return (n**0.5)%1==0
    for a in range(int(c**0.5)+1):
        # print(a,c,c-a**2)
        if(isI(c-(a**2))):
            print(a,(c-(a**2))**0.5,c)
            return True
    return False

print(soln(5),True)
print(soln(3),False)
print(soln(4),True)
print(soln(2),True)
print(soln(1),True)
print(soln(20),True)