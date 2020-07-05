import math

def soln(numStr):
    if(numStr <= "1"): return 0
    num= int(numStr)
    numLog= math.log(num,2)
    return int(numLog%1 == 0)

def soln2(A):
    Aint = int(A)
    if(Aint <= 1): return 0
    while(Aint>1):
        if(Aint%2 == 0):
            Aint //= 2
        else:
            return 0
    return 1

if __name__ == "__main__":
    for i in range(25):
        print(i,soln(str(i)))
    print(soln("5070602400912917605986812821504"))