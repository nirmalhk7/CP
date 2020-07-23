
def soln(A):
    def recursive(A):
        if(len(A)>1):
            firstLen=len(A[0])
            secondLen= len(A[1])
            ans=['']*firstLen*secondLen
            k=0
            for i in range(firstLen):
                for j in range(secondLen):
                    ans[k]=A[0][i]+A[1][j]
                    k+=1
                    # print(i*j,A[0][i]+A[1][j],ans)
            A[0]= ans
            del A[1]
            recursive(A)
        return A[0]

    hash_phone={
        '0':['0'],
        '1':['1'],
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']}
    if(len(A)==1): return hash_phone[A[0]]

    combination_list= []
    for i in A:
        combination_list+= [hash_phone[i]]
    return recursive(combination_list)

def soln2(A):
    hash_phone={
        '0':['0'],
        '1':['1'],
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']}
    
    if(len(A)==1): return hash_phone[A[0]]
    ans= []
    restCombinations= soln2(A[1:])
    for j in hash_phone[A[0]]:
        for k in restCombinations:
            ans.append(j+k)
    # print(A,restCombinations,ans)
    return ans
if __name__ == "__main__":
    # import time
    # a=[1,2,3]
    # stx= time.time()
    print(soln2("239"))
    print(soln("239"))
    # print(time.time()-stx)