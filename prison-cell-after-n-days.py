
def soln(Arr,N):
    A=Arr.copy()
    for i in range(N):
        print(Arr)
        A[0]=0
        A[7]=0
        for i in range(len(A)):
            if(i==0 or i==len(A)-1):
                pass
            else:
       #         print("Comparing A[",i-1,"]=",A[i-1]," and A[",i+1,"]=",A[i-1])
                if(Arr[i-1]==Arr[i+1]):
            #        print("SWAPSED")
                    A[i]=1
                else:
                    A[i]=0
        Arr=A
    return Arr

def soln2(Arr,N):
    cArr=Arr.copy();
    if(N>0):
        Arr[0]=0
        Arr[7]=0
        for i in range(len(Arr)):
            try:
                cArr[i]=int(Arr[i-1]==Arr[i+1])
            except IndexError:
                cArr[i]=0
        N-=1
    return soln2(cArr,N)

def soln3(A,N):
    for i in range(N):
        changed=[False  for i in range(8)]
        changed[0],changed[7]=A[0]==1,A[7]==1
        changed[1]=A[0]==A[2]!=A[1]
        
        for inx in range(len(changed[1:-1])):
            changed[inx+1]=A[inx]==A[inx+2] and A[inx+1]!=1
        print(A,changed)
        for j in range(len(changed)):
            if(changed[j]):
                A[j]= int(A[j]==0)

def soln4(A,N):
    for i in range(N):
        Acopy=[0 for i in range(8)]
        Acopy[0],Acopy[7]=0,0
        Acopy[1]= int(Acopy[0]==Acopy[2])
        Acopy[2]= int(Acopy[0]==Acopy[2])
        Acopy[3]= int(Acopy[0]==Acopy[2])
        Acopy[4]= int(Acopy[0]==Acopy[2])
        Acopy[5]= int(Acopy[0]==Acopy[2])
        Acopy[6]= int(Acopy[0]==Acopy[2])
        
        for i in range(len(A[1:-1])):
            Acopy[i+1]= int(A[i]==A[i+2])
      #  print(A,Acopy)
        A=Acopy
    return A

def next_calc(A):
    res = [0 for i in range(8)]
    for i in range(1,7):
        res[i]=int(A[i-1]==A[i+1])
    return res

def soln5(A,N):
    loop_check={}
    for i in range(N):
        if str(A) in loop_check:
            return soln5(A,(N-i)%(i-loop_check[str(A)]))
        else:
            loop_check[str(A)]=i
            A=next_calc(A)
    return A
if __name__ == "__main__":
    print("ANS",soln5([0,1,0,1,1,0,0,1],7))
    print("ANS",soln5([0,0,1,1,1,1,1,0],1000000000))