



def soln(A,B):
    from itertools import combinations 
    def print_powerset(string,limit): 
        ans=[]
        for i in range(0,len(string)+1): 
            for element in combinations(string,i): 
                if(len(list(element))>=B):
                    ans.append(list(element))
        return ans
    odd_hsx={}
    for i in range(len(A)):
        if(A[i]%2!=0):
            odd_hsx[i]=True
            A[i]=1
        else:
            A[i]=0
    # If odd numbers are too few.
    if(len(odd_hsx)<B): return 0
    # If first and last numbers are among the odd numbers.
    elif(0 in odd_hsx and len(A)-1 in odd_hsx and B>1):
        if(odd_hsx[0] and odd_hsx[len(A)-1]):
            return 1
    # print(odd_hsx)

    subsets= print_powerset(A,B)
    ans=0
    for i in range(len(subsets)):
        if(sum(subsets[i])==B):
            ans+=1
    return ans//2
    


def soln2(A,B):
    odd_hsx={}
    oddCount=0
    for i in range(len(A)):
        if(A[i]%2!=0):
            odd_hsx[i]=True
            A[i]=0
            oddCount+=1
        else:
            odd_hsx[i]=False
            A[i]=1
    if(oddCount<B): return 0
    elif(odd_hsx[0] and odd_hsx[len(A)-1]): return 1

    curr_sum=0
    res=0
    prevSum={}
    for i in range(len(A)):
        curr_sum+= A[i]
        if(curr_sum == B):
            res+=1
        
        if curr_sum-B in prevSum:
            res += prevSum[curr_sum-B]

        if(curr_sum not in prevSum):
            prevSum[curr_sum]=1
        else:
            prevSum[curr_sum]+=1
    return res



def complete_ans(A,B):
    n= len(A)
    count =0 
    odd= 0
    prefix= [0]*(n+1)
    for i in range(n):
        prefix[odd]+=1
        if(A[i]&1):
            odd+=1
        if(odd>=B):
            count+= prefix[odd-B]
    return count
if __name__ == "__main__":
    # print(print_powerset([1,2,3]))
    print(compl([4, 3, 2, 3, 4],2),4)
    print(soln2([5, 6, 7, 8, 9],3),1)