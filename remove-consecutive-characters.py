
def soln(A,B):
    hx={}
    for i in range(len(A)):
        if A[i] not in hx:
            hx[A[i]]=[i,1]
        else:
            hx[A[i]][1]+=1
    answer=""
    print(hx)
    for i in range(len(A)):
        if(hx[A[i]][1]!=B):
            answer+= A[i]
    return answer

def soln2(A,B):
    from itertools import groupby
    def longestkcon(arr,k):
        res=''
        for c,g in groupby(arr):
            l=len(list(g))
            if l<k:
                res+=c*l
            elif l==k:
                res+=''
            else:
                res+=c*(l-k)
        return res
    return longestkcon(A,B)
if __name__ == "__main__":
    print(soln2("aaabbbccd",2))
    print(soln2("aabcd",2))
    print(soln2("aabbccd",2))
    print(soln2("abcddcbsa",2))
