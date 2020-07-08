
def soln(A):
    start_row, start_col= 0, 0
    cur_col=cur_row=0
    max_col_pos=0
    ans= []
    while True:
        temp=[]
        if(cur_col==max_col_pos):
            ans.append(temp)
    
    return ans

def soln2(A):
    mxrow = 2*len(A)-2
    mat = [[] for i in range(mxrow+1)]
    # print("MXROW",mxrow,mat)
    for i in range(len(A)):
        for j in range(len(A)):
            mat[i+j].append(A[i][j])
    return mat
if __name__ == "__main__":
    ans= soln2([[1,2,3],[4,5,6],[7,8,9]])
    for i in ans:
        print(i)