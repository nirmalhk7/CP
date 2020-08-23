
def soln(A,B):
    ans= []
    def r(s,v,A,B):
        # prevv=v;
        v=v*10+s
        # print("Checking V",v,s,prevv)
        if(A<=v<=B): ans.append(v)
        elif(v>B): return
        if(s!=0): r(s-1,v,A,B)
        if(s!=9): r(s+1,v,A,B)

    if(A==0): ans.append(0)
    for i in range(1,10):
        r(i,0,A,B)
    ans.sort()
    return ans
if __name__ == "__main__":
    print(soln(10,20))