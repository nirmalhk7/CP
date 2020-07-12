
def soln(A):
    Alen=len(A)
    for i in range(Alen//2):
        temp=A[i]
        A[i]=A[Alen-i-1]
        A[Alen-i-1]=temp
        # print(A)
    return A

if __name__ == "__main__":
    print(soln(['A','B','C','D','E']))