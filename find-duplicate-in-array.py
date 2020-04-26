def repeatedNumber(A):
    Arep=[0 for i in range(max(A)+1)]
    for i in range(len(A)):
        Arep[A[i]]+=1
        if(Arep[A[i]]>1):
            return A[i]
    
if __name__ == "__main__":
    A=[1,2,3,4,5,1]
    print(repeatedNumber(A))