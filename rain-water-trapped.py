def soln(A):
    left, right= [0]*len(A), [0]*len(A)
    mx= -99999999999999
    for i in range(len(A)):
        mx=max(mx,A[i])
        left[i]=mx
    mx= -99999999999999
    for i in range(len(A)):
        mx= max(mx,len(A)-1-A[i])
        right[i]= mx
    water= 0
    for i in range(len(A)):
        water+= min(left[i],right[i])-A[i]
    return water

def soln2(A):
    stack=[]
    nsum, nmin= 0, -1
    for i in range(len(A)):
        if(stack==[] or A[stack[-1]]>A[i]):
            stack.append(i)
        else:
            nmin=-1
            while(stack!=[] and A[stack[-1]]<=A[i]):
                if(nmin==-1): nsum+= (A[stack[-1]]-A[nmin])*(i-stack[-1]-1)
                nmin= stack[-1]
                stack.pop()
            if(stack!=[]):
                nsum+= (A[i]-A[nmin])*(i-stack[-1]-1)
            stack.append(i)
    return nsum

if __name__ == "__main__":
    print(soln2([0,1,0,2,1,0,1,3,2,1,2,1]))