

def soln(A,B):
    x= -1
    try:
        x= A.index(B)
    except ValueError:
        x= -1
    return x
if __name__ == "__main__":
    print(soln([4, 5, 6, 7, 0, 1, 2, 3],4))
    pass