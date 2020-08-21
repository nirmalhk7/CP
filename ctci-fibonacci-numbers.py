
def soln(n):
    if(n<=1): return n
    return soln(n-1)+soln(n-2);

if __name__ == "__main__":
    print(soln(6))