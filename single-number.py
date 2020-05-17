def singleNumber(A):
    x = 0
    
    for n in A:
        x = x ^ n
        print(x,n)
    return x

if __name__ == "__main__":
    print(singleNumber([1, 2, 2, 3, 1]))