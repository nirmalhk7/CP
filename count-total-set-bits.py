
# def soln(A):
#     count= 0
#     for i in range(1,A):
#         lx= len(bin(i).split('b')[1])
#         print(lx,bin(i).split('b')[1],i)
#         count+= lx
#     return count

def soln(A):
    def countBits(A):
        if(A==0): return A
        m= 0
        while A>1:
            m+= 1
            A= A >> 1
        if(A==((1<<(m+1))-1)): return ((m+1)*(1<<m))
        A=A-(1<<m)
        return (A+1)+(m*(1<<(m-1)))
    return countBits(A)%1000000007
if __name__ == "__main__":
    print(soln(12))