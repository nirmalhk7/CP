def soln(A,B):
    n=len(A)
    if(n<=2): return n
    m = 0
    for i in range(n):
        l={}
        dup = 1
        for j in range(n):
            if(A[i]==A[j] and B[i]==B[j] and i!=j):
                dup+=1
            elif i!=j:
                if(A[i]==A[j]):
                    l['v']=l.get('v',0)+1
                elif (B[i]==B[j]):
                    l['h']=l.get('h',0)+1
                else:
                    slope = 1.0 * (B[i]-B[j])/(A[i]-A[j])
                    l[slope] = l.get(slope,0)+1
        if(len(l)>0):
            m = max(m,max(l.values())+dup)
        else:
            m = max(m,dup)

if __name__ == "__main__":
    print(soln([1,2],[1,2]))