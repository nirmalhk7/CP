
def soln(A):
    sumNum=0
    if(A>9):
        while A!=0:
            sumNum+= A%10
            A//=10
        soln(sumNum)
    if(sumNum>0): return sumNum
    return A
    
def soln2(A):
    sumNum=0
    while A!=0:
        sumNum+= A%10
        A//=10
        # print("X",sumNum,A)
        # input()
        if(A==0 and sumNum<10):
            return sumNum
        if(A==0): 
            A=sumNum
            sumNum= 0
    return sumNum

if __name__ == "__main__":
    print(soln2(38))
    print(soln2(432))