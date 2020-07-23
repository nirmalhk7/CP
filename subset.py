
def subset(A, currIndex=0,currSub=[],answer=[],maxIndex=1):
    if(currIndex>=maxIndex):
        answer.append(currSub)
        print(answer,"currIndex",currIndex,"maxIndex",maxIndex)
        currSub=[]
        if(0<maxIndex<=len(A)):
            maxIndex+=1
        else:
            maxIndex-=1
    else:
        currSub.append(A[currIndex])
        answer,currSub= subset(A,currIndex+1,currSub,answer)
        if(len(currSub)>0):
            currSub.pop(-1)
    return answer,currSub

def subset2(A,currIndex=0, currSub=[],answer=[]):
    answer.append(currSub)
    print(currSub)
    for i in range(currIndex,len(A)):
        currSub.append(A[i])
        subset2(A,i+1,currSub,answer)
        currSub.pop(-1)

def subset3(A):
    res= []
    A.sort()
    def f(A,subset=[],index=0):
        print("APP",subset[:])
        res.append(subset[:])
        for i in range(index,len(A)):
            subset.append(A[i])
            f(A,subset,i+1)
            x=subset.pop(-1)
            print("POP",subset,x)
        return
    f(A)
    return res
if __name__ == "__main__":
    print("ANS",subset3([1,2,3,4]))