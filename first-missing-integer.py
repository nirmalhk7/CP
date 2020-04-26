def firstMissingPositive(A):
    indexArr=[0 for i in range(max(A))]
    for i in range(len(A)):
        if(A[i]>0):
            indexArr[A[i]-1]=1
            print(A,indexArr)
    if(len(indexArr)>0):
        for i in range(len(indexArr)):
            if(indexArr[i]==0):
                print("X")
                return i+1
        print("y")
        return len(indexArr)+1
    return 1;

if __name__ == "__main__":
    print(firstMissingPositive([1,3,-4]))