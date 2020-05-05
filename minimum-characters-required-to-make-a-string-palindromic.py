def solve(A):
    mirrorMiddleChars=[]
    for i in range(len(A)):
        if(i!=0 and i!=len(A)-1):
            if(A[i-1]==A[i+1]):
                mirrorMiddleChars.append(i)
    print(mirrorMiddleChars)

if __name__ == "__main__":
    print(solve("banana"))