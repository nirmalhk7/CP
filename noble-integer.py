def soln(A):
    A.sort()
    answer=[]
    for i in range(len(A)):
        if(len(A[i+1:])==A[i]):
            answer.append(A[i])
    if(len(answer)>0): return 1
    else: return -1

# sort(A.begin(), A.end());

# for(int i=0;i<A.size();i++)
# {
# if(A[i]==A[i+1] && i!=A.size()-1)
# {
# continue;
# }
# if(A[i]==A.size()-1-i)
# return 1;
# }
# return -1;

def soln2(A):
    A.sort()
    for i in range(len(A)):
        if(i!=len(A)-1):
            if(A[i]==A[i+1]):
                continue
        if(A[i]==len(A)-1-i):
            return 1
    return -1

if __name__ == "__main__":
    print(soln2([3,2,1,3]))
    print(soln2([1,1,3,3]))
    print(soln2([1, 2, 7, 0, 9, 3, 6, 0, 6]))
