
def soln(A):
    answer=[-1 for i in range(len(A))]
    for i in range(1,len(A)):
        xa= A[:i].copy()
        # print("xa",xa,A[i])
        for j in range(len(xa)):
            if(xa[j]<A[i]):
                answer[i]= xa[j]
    return answer

def soln2(A):
    lenA= len(A)
    answer=[-1 for i in range(lenA)]
    for i in range(1,lenA):
        xa= A[:i].copy()
        lenxa= len(xa)
        # print("xa",xa,A[i])
        for j in range(len(xa)):
            if(xa[j]<A[i]):
                answer[i]= xa[j]
    return answer


if __name__ == "__main__":
    import time
    stx= time.time()
    print(soln([34,35,27,42,5,28,39,20,28]))
    print("ET",time.time()-stx)
    stx= time.time()
    print(soln2([34,35,27,42,5,28,39,20,28]))
    print("ET",time.time()-stx)
