from Tree import *

arx=[]
def soln(A,num):
    global arx
    if(A):
        print(arx)
        arx.append(A.val)
        if(A.val!=num):
            soln(A.left,num)
            soln(A.right,num)
        else:
            return arx
    else:
        arx.pop()
    return arx

def solve(A,b,ans):
    if(A==None):
        return False,ans
    if(A.val==b):
        return True,ans
    if(A.left):
        ans.append(A.right.val)
        if(solve(A.left,b,ans)):
            return True,ans
        ans.pop()
    if(A.right):
        ans.append(A.right.val)
        if(solve(A.right,b,ans)):
            return True
        ans.pop()
    return False,ans

def soln2(A,B):
    ans=[]
    ans.append(A.val)
    res,ans = solve(A,B,ans)
    return ans
if __name__ == "__main__":
    # printTree(init([[2,None,None],[3,None,None],[1,2,3,"ROOT"]]))
    print(soln(init([[2,None,None],[3,None,None],[1,2,3,"ROOT"]]),3))
    # print(init([[2,None,None],[3,None,None],[1,2,3,"ROOT"]],3))
    pass