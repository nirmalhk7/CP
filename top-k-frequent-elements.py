
def soln(A,B):
    A.sort()
    answer={}
    for i in range(len(A)):
        if(A[i] not in answer):
            answer[A[i]]=1
        else:
            answer[A[i]]+=1
    answer= sorted((value) for (key,value) in answer.items())[:B]
    return answer
    # ans= []
    # for i in range(len(answer)):
    #     ans.append(answer[i][1])
    # return ans
    
def soln2(A,B):
    um= {}
    n=len(A)
    for i in range(n):
        if(A[i] in um):
            um[A[i]]+= 1
        else:
            um[A[i]]=  1
    a= [0]*len(um)
    j= 0
    for i in um:
        a[j]= [i, um[i]]
        j+= 1
    a= sorted(a, key= lambda x: x[0],reverse= True)
    a= sorted(a, key= lambda x: x[1],reverse= True)
    ans= [0]*B
    for i in range(B):
        ans[i]=a[i][0]
    return ans

if __name__ == "__main__":
    print(soln2([1,2,1,2,1,3],2))
    print(soln2([-1,-1],1))