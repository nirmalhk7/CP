from BinaryTree import *


def soln(A):
    def sumleaf(root,sumx=0,ans=0):
        if(not root):
            return
        sumx=(sumx*10+root.val)%1003
        if(not root.left and not root.right):
            ans+=sumx
            sumx/=10
            return
        sumleaf(root.left,sumx,ans)
        sumleaf(root.left,sumx,ans)
        sumx/=10
    ans= 0
    sumleaf(A,0,ans)
    return ans%1003
if __name__ == "__main__":
    head= TreeNode(1)
    head.left= TreeNode(2)
    head.left.left= TreeNode(4)
    head.left.right= TreeNode(5)
    head.right= TreeNode(3)
    head.right.left= TreeNode(6)
    head.right.right= TreeNode(7)
    print(soln(head))
    pass