from BinaryTree import *

def soln(head):
    def r(root,parent=None):
        if(root!=None):
            r(root.left,root)
            r(root.right,root)
            if(root.right and not root.left):
                # print("Found",root.val,root.right.val)
                root.val= root.right.val
                root.left= root.right.left
                root.right= root.right.right
            elif(root.left and not root.right):
                # print("Found",root.val,root.left.val)
                root.val= root.left.val
                root.right= root.left.right
                root.left= root.left.left

        return root
    return r(head)
if __name__ == "__main__":
    head= TreeNode(1)
    head.right= TreeNode(2)
    head.left= TreeNode(3)
    head.right.left= TreeNode(4)
    head.right.right= TreeNode(5)
    head.left.right= TreeNode(6)
    printBT(soln(head))