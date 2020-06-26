def solution(A):
    Ahash = {}
    for i in A:
        try:
            if(Ahash[i]): return i
        except:
            Ahash[i]=True

def solution2(A):
    A.sort()
    for i in range(len(A[:-1])):
        if(A[i]==A[i+1]):
            return A[i]

if __name__ == "__main__":
    print(solution2([1,3,4,4,5,2]))