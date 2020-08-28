maximum=1

def soln(A):    
    def recursion(n=len(A)):
        global maximum
        if n==1:
            return 1
        maxEnd= 1
        for i in range(1,n):
            if(A[i-1]<A[n-1]):
                maxEnd= max(recursion(i),maxEnd)
        maximum= max(maxEnd,maximum)
        return maxEnd
    
    return recursion()

if __name__ == "__main__":
    print(soln([10, 22, 9, 33, 21, 50, 41, 60, 80]))