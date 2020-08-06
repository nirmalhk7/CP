
def soln(A):
    qx=[]
    for i in range(len(A)):
        if(A[i]==0):
            if(i+1<len(A)):
                qx.append(A[i+1])
                


if __name__ == "__main__":
    print(soln([1,0,2,3,0,4,5,0]))