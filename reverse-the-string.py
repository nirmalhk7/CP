def solve(A):
    Z=A.split(' ')
    Z.reverse()
    opsx=""
    for i in range(len(Z)):
        if(Z[i]!=''):
            opsx+=' '+Z[i]
    return opsx[1:]
if __name__ == "__main__":
    print(solve("The sky is blue"))