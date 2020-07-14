def soln(A):
    if(len(A)<3):
        raise ValueError("fcd")
    highest= max(A[0],A[1])
    lowest = min(A[0],A[1])
    highest_pdt_2= A[0]*A[1]
    lowest_pdt_2 = A[0]*A[1]
    highest_pdt_3= A[0]*A[1]*A[2]
    for i in range(2,len(A)):
        current= A[i]
        highest_pdt_3= max(highest_pdt_3,current*highest_pdt_2,current*lowest_pdt_2)
        highest_pdt_2= max(highest_pdt_2,current*highest)
        lowest_pdt_2 = min(lowest_pdt_2,current*highest,current*lowest)
        highest= max(highest, current)
        lowest = max(lowest,current)
    return highest_pdt_3
if __name__ == "__main__":
    print(soln([1,5,3,9,6]))
    print(soln([-10,-10,1,3,2]))