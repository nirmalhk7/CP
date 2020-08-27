
def soln(A,B):
    if(len(B)==0):
        return int(A==0)
    dp=[[False for i in range(len(B)+1)] for j in range(len(A)+1)]
    dp[0][0]= True

    for j in range(1,len(B)+1):
        if(B[j-1]=="*"):
            dp[0][j]=dp[0][j-1]
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if(B[j-1]==)

    return dp
if __name__ == "__main__":
    print(soln("aa","*"),1)
    pass