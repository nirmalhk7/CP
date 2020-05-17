def getZeroCount(A):
    zeroCount=0
    for a in range(A):
        if(a==0):
            zeroCount+=1
    return zeroCount

def howManyAhead(A):
    zeroAhead=0
    oneAhead=0
    for a in range(A):
        if(a==1):
            break
        else:
            zeroAhead+=1
    for a in range(A):
        if(a==1):
            break
        else:
            oneAhead+=1
    return zeroAhead,oneAhead

def maxone(A,B):
    # If B is more than eq to num of zeros
    if(B>=getZeroCount(A)):
        return [i for i in range(len(A))]
    # Else
    start=0
    end=0
    flipCount=0
    for i in range(len(A)):
        if(A[i]==1):
            end+=1
        else:
            # If less zeros than what we need
            zAhead,oAhead = howManyAhead(A[i:])
            if(zAhead<=B):
                flipCount+=zAhead
                end+=zAhead+oAhead
                


                

if __name__ == "__main__":
    print(maxone([1,1,0,1,1,0,0,1,1,1],3))
    print(maxone([1,0,0,1,1,0,0,1,1,1],3))
    print(maxone([1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0],4))
