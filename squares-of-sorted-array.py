def soln(A):
    for i in range(len(A)):
        A[i]**=2
    return sorted(A)
if __name__ == "__main__":
    print(soln([-7,-3,2,3,11]))