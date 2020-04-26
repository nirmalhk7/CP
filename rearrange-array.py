def arrange(A):
    B=A.copy()
    for i in range(len(A)):
        #print("Replacing A["+str(i)+"]="+str(A[i])+" with B["+str(A[i])+"]="+str(B[A[i]]))
        A[i]=B[A[i]]
    return A

if __name__ == "__main__":
    A=[4,0,2,1,3]
    print(arrange(A))