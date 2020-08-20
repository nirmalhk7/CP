from BinaryTree import *

def soln(A,sumx):
    def r(head,ans,height=0):
        if(head!=None):
            r(head.left,ans,height+head.val)
            if(not head.left and not head.right):
                print("HX",height+head.val,sumx)
                if(height+head.val==sumx):
                    ans=True
            r(head.right,ans,height+head.val)
        return ans or False
    return r(A)

if __name__ == "__main__":
    head=TreeNode(5)
    head.left=TreeNode(4)
    head.left.left=TreeNode(11)
    head.left.left.left=TreeNode(7)
    head.left.left.right= TreeNode(2)
    head.right=TreeNode(8)
    head.right.right=TreeNode(4)
    head.right.right.right=TreeNode(1)
    head.right.left=TreeNode(13)

    print(soln(head,22))