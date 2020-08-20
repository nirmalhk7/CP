
def soln(A,B):
    if(B>len(A)): return []
    ans=[None for i in range(len(A)-B+1)]
    return ans

if __name__ == "__main__":
    print(soln([1,2,1,3,4,3],3))
    print(soln([1,1,2,2],1))