
def soln(A,B):
    return 2*min(min(A,B)-1,8-max(A,B))+7;

if __name__ == "__main__":
    print(soln(4,4))