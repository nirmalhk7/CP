def soln(N):
    uglyArr = [1,2,3,4,5]
    uglyNum = [2,3,5]
    uglyCheck = {1:True,2:True,3:True,4:False,5:True}
    counter = 1
    while(N>len(uglyCheck)):
        # N is unevaluated
        if(not bool(uglyCheck.get(counter)) and uglyCheck.get(counter/2) or uglyCheck.get(counter/3) or uglyCheck.get(counter/5)):
                uglyCheck[counter]=True
        counter += 1
    uglyList = list(uglyCheck.keys())

    return uglyList[N-1]

def soln2(N):
    if N==1: return 1
    x2 = x3 = x5 = 0
    ugly = [0]*N
    ugly[0]=1
    for i in range(1,N):
        ugly[i]=min(ugly[x2]*2,ugly[x3]*3,ugly[x5]*5)
        if ugly[i]==ugly[x2]*2: x2+=1       
        if ugly[i]==ugly[x3]*3: x3+=1
        if ugly[i]==ugly[x5]*5: x5+=1
    return ugly[-1]
if __name__ == "__main__":
    print(soln2(10))