
def soln(A):
    A.sort(reverse=True)
    largest3=[A[0],A[1],A[2]]
    smallest2=[A[-1],A[-2]]
    print(largest3,smallest2)
    return max(smallest2[0]*smallest2[1]*largest3[0],largest3[0]*largest3[1]*largest3[2])

if __name__ == "__main__":
    print(soln([0, -1, 3, 100, 70, 50]),350000)
    print(soln([-1000,0,-1,3,10,7,50]),50000)
    print(soln([1, 2, 3, 4]),24)