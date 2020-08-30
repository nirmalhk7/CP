def soln(n,k):
    def recursive(n,k):
        print("N=",n,"K=",k)
        if (n == 1): 
            return 1
        else: 
            return (recursive(n - 1, k) + k-1) % n + 1

    return recursive(n,k)
    
if __name__ == "__main__":
    print(soln(n=5,k=2))