from BinaryTree import *

def soln(A,B):
    def recursion(Aptr,Bptr):
        if(not Aptr and not Bptr):
            return None
        if(not Aptr):
            return Bptr
        if(not Bptr):
            return Aptr
        root= TreeNode(Aptr.val+Bptr.val)
        root.left= recursion(Aptr.left,Bptr.left)
        root.right= recursion(Aptr.right, Bptr.right)
        return root
    return recursion(A,B)

if __name__ == "__main__":
    A= TreeNode(2)
    A.left= TreeNode(1)
    A.right= TreeNode(4)
    A.left.left= TreeNode(5)
    A.left.left.left= TreeNode(1)

    B= TreeNode(3)
    B.left= TreeNode(6)
    B.right= TreeNode(1)
    B.left.right= TreeNode(2)
    B.right.right= TreeNode(7)
    printBT(soln(A,B))
    pass