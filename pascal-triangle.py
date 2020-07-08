
def soln(A):
    fans=[[1],[1,1]]
    if(A==0): return []
    if(A==1): return [fans[0]]
    if(A==2): return fans
    for i in range(A):
        i=i+1
        if(i>2):
            tans=[]
            for j in range(i):
                if(j!=0 and j!=i-1):
                    tans.append(fans[i-2][j]+fans[i-2][j-1])
                else:
                    tans.append(1)     
            fans.append(tans)
    return fans
if __name__ == "__main__":
    ans=soln(2)
    print("++++")
    for i in ans:
        print(i)