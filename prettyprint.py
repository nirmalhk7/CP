def soln(A):
    ans=[[0 for j in range(1+A)] for i in range(A+1)]
    for i in range(len(ans)):
        for j in range(len(ans)):
    return ans

if __name__ == "__main__":
    arx=soln(4)
    for i in arx:
        for j in i:
            print(j,end=" ")
        print("")