
def soln(A,B):
    def lsx(i,j,d):
        if i<0 or j<0:
            return 0
        
        if d.get(str(i)+'_'+str(j)):
            return d.get(str(i)+'_'+str(j))
        result = max(
            lsx(i-1,j-1,d)+1 if A[i]==B[j] else 0,
            lsx(i-1,j,d),
            lsx(i,j-1,d)
        )
        d[str(i)+'_'+str(j)]= result
        return result
    
    return lsx(len(A)-1,len(B)-1,{})

if __name__ == "__main__":
    print(soln("abbcdgf","bbadcgf"))

    # if for some (i, j) A[i] = B[j]
    # , then one of the possible longest commen subsequence can be Longest commen subsequence 
    # of(A[1..i-1], B[1....j-1]) + A[i] +  Longest commen subsequence of(A[i+1....n], B[j+1....m])
