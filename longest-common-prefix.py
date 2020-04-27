def longestCommonPrefix(A):
    k=2
    ans=""
    ansmark=0
    if(len(A)>=2):
        for i in range(len(A[0]) if len(A[0])>len(A[1]) else len(A[1])):
            if(A[0][:i]==A[1][:i]):
                ans=A[0][:i]
                ansmark=i
                print(A[0],A[1],A[0][:i],A[1][:i],ans)
        while k!=len(A):
            while(ans!="" and ans!=A[k][:ansmark]):
                ans=ans[:-1]
                ansmark-=1
            k+=1
    return ans

if __name__ == "__main__":
    print("Answer", longestCommonPrefix([ "abcd", "abcd", "efgh" ]))