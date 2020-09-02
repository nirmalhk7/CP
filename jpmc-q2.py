from BinaryTree import *

def soln(root):
    def recursive(root):
        if(root.left or root.right):
            leftValue= recursive(root.left)[1]
            rightValue= recursive(root.right)[1]
            oldValue= root.val
            print("ITR",leftValue,rightValue,oldValue)
            root.val= rightValue+leftValue
            return root, oldValue + leftValue + rightValue
        elif(root):
            oldValue= root.val
            root.val= 0
            return root,oldValue
        return root, 0
    printBT(recursive(root)[0])

if __name__ == "__main__":
    x= TreeNode(7)
    x.left= TreeNode(5)
    x.right= TreeNode(11)
    x.left.left= TreeNode(2)
    x.left.right= TreeNode(6)
    x.right.left= TreeNode(9)
    x.right.right= TreeNode(15)
    soln(x)