from BinaryTree import *

def soln(A):
    def r(head):
        if(head!=None):
            if(head.left or head.right):
                if(not head.left):
                    head.left=head.right
                    head.right=None
                elif(not head.right):
                    head.right=head.left
                    head.left= None
                else:
                    temp= head.right
                    head.right= head.left
                    head.left= temp
            r(head.left)
            r(head.right)
        return head
    return r(A)
if __name__ == "__main__":
    head= TreeNode(1)
    head.left= TreeNode(2)
    head.left.left= TreeNode(4)
    head.left.right= TreeNode(5)
    head.right= TreeNode(3)
    head.right.left= TreeNode(6)
    head.right.right= TreeNode(7)

    printBT(soln(head))
    pass