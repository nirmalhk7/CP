
def soln(A):
    ans_hsx={}
    for i in range(len(A)):
        A[i]="".join(sorted(A[i]))
        try:
            ans_hsx[A[i]].append(i+1)
        except:
            ans_hsx[A[i]]=[i+1]
    return list(ans_hsx.values())

if __name__ == "__main__":
    print(soln(["cat","dog","god","tca"]),[[1,4],[2,3]])