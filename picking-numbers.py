
def soln(A):
    A.sort()
    Acount={}
    for i in A:
        try:
            Acount[i]+=1
        except:
            Acount[i]=1
    Aposition={}
    for i in range(len(A)):
        Aposition[A[i]]=i
    print(A,Acount,Aposition)
    maxValue= 0
    for i in range(len(A)):
        checkFrom= i+1
        value= 1
        for j in range(checkFrom,len(A)):
            if(abs(A[i]-A[j])<=1):
                value+=1
        maxValue= max(value,maxValue)
    return maxValue



if __name__ == "__main__":
    A= [4,6,5,3,3,1]
    A= [1,2,2,3,1,2]
    print(soln(A))