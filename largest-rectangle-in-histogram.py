
def soln(A):
    def prevSmaller(A):
        ans=[-1]
        lenA= len(A)
        for i in range(1,lenA):
            if(A[i-1]<A[i]):
                ans.append(i-1)
            else:
                j=i-1
                while(j>0 and A[ans[j]]>=A[i]):
                    ans.append(ans[j])
                    j-=1
    def nextSmaller(A):
        lenA= len(A)
        ans=
    pass
if __name__ == "__main__":
    print(soln([2, 1, 5, 6, 2, 3]))