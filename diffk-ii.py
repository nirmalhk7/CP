
def soln(A,B):
    hsx={}
    ans=0
    for i in range(len(A)):
        hsx[A[i]]=i
    for i in range(len(A)):
        print(A[i],"FINDING",abs(B-A[i]),hsx)
        if(abs(B-A[i]) in hsx):
            if(hsx[abs(B-A[i])]!=i):
                print("FOUND",abs(B-A[i]))
                ans=1
    return ans

# def soln2(A,B):
#     hsx={}
#     for i in range(len(A)):
        

        # if(B-A[i] not in hsx):
if __name__ == "__main__":
    # print(soln([1,5,3],2))
    print(soln([34,63,64,38,65,83,50,44,18,34,71,80,22,28,20,96,33,70,0,25,64,96,18,2,53,100,24,47,98,69,60,55,8,38,72,94,18,68,0,53,18,30,86,55,13,93,15,43,73,68,29],97))
    # print(soln())