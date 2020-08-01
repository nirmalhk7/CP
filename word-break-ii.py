
def soln(A,B):
    startBreakPoint=0
    ans=[]
    if(len(A)==0): return A
    for i in range(1,len(A)):
        print("CHECKING",A[startBreakPoint:i],A[i])
        if(A[startBreakPoint:i+1] in B):
            ans.append(A[startBreakPoint:i+1])
            startBreakPoint=i+1
            # print("YES",startBreakPoint)
    return ans

def soln2(A,B):
    def populate_wmap()
    populate_wmap(len(A),B)

if __name__ == "__main__":
    print(soln("catsanddog",["cat", "cats", "and", "sand", "dog"]))