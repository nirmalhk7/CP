def maxSpecialProduct(A):
    for i in range(len(A)):
        a=A.copy();
        a.sort(reverse=True);
        b=A.copy();
        b.sort();
        while (a[-1]<=A[i]):
            a.pop()
        while ()
        lsval=0
        if(len(a)!=0):
            lsval=a[-1]
        print("LSVAL",lsval,A[i])
        print("RSVAL",rsval,A[i])

        

if __name__ == "__main__":
    print(maxSpecialProduct([1,2,4,2]))