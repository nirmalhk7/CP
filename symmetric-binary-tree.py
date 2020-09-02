from BinaryTree import *

def soln(A):
    def requireNonNull(ptr):
        if(ptr): return str(ptr.val)
        return "x"

    def recursive(rootLeft,rootRight,ans=True):
        if(rootLeft is None and rootRight is None):
            return 1
        if(rootLeft and rootRight):k;
            if(rootLeft.val!=rootRight.val):
                return False
            ans= ans and recursive(rootLeft.left,rootRight.right)
            ans= ans and recursive(rootLeft.right,rootRight.left)
        return ans
    return recursive(A.left,A.right)

if __name__ == "__main__":
    head= TreeNode(1)
    head.left= TreeNode(2)
    head.right= TreeNode(2)
    head.left.left= TreeNode(3)
    head.left.right= TreeNode(4)
    head.right.left= TreeNode(4)
    head.right.right= TreeNode(3)
    print(soln(head))
    pass