def nextZero(start=0,arr=None):
    for i in range(start,len(arr)):
            if(arr[i]==0):
                return i

def maxone(A, B):
    zeroCount=0
    for i in range(len(A)):
        if(A[i]==0): zeroCount+=1
    if(B>=zeroCount):
        return [i for i in range(len(A))]
    count,tempCount,n=0,0,B
    start,tempStart=0,0
    end=0
    zeroPointer=nextZero(arr=A)
    for i in range(len(A)):
        if(A[i]==1):
            tempCount+=1
            continue
        else:
            if n>0:
                n-=1
                tempCount+=1
                continue
            else:
                if tempCount>count:
                    count=tempCount
                    start=tempStart
                    end=i
                n=B
            tempCount=0
            i=zeroPointer+1
            zeroPointer= nextZero(zeroPointer+1,A)
            print("Next zero at",zeroPointer)
            print("Seen "+str(tempCount)+" ones!")
            

    if(tempCount>count):
        count=tempCount
        start=tempStart
        end=i-1
    return [i for i in range(start,end)]


if __name__ == "__main__":
    print(maxone([1,1,0,1,1,0,0,1,1,1],3))
    print(maxone([1,0,0,1,1,0,0,1,1,1],3))
    print(maxone([1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0],4))
    pass