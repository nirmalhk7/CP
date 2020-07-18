
def soln(A,B):
    A+= B
    A= sorted(A)
    Alen= len(A)
    if(Alen%2!=0):
        return A[Alen//2]
    else:
        return (A[Alen//2]+A[(Alen//2)-1])/2
    return A

def soln2(A,B):
    m= len(A)
    n= len(B)
    if(m>n): return soln2(B,A)
    l,r = 0,m
    while l<=r:
        partx= l+(r-l)/2 - party
        party= 

if __name__ == "__main__":
    print(soln([1,4],[2,3]))
    print(soln([ ],[20]))
    print(soln([0,23],[]))
    print(soln([],[0,23]))