from BinaryTree import *

def soln(A,B):
    def r(root,parent=None,arx=[],height=0):
        if(root!=None):
            if(root.val==B):
                if(parent):
                    if(parent.left==root): parent.right=None
                    
                else:
                    return arx
            r(root.left,parent,arx,height+1)
            r(root.right,parent,arx,height+1)
        return root

if __name__ == "__main__":
    x= TreeNode(1)
    x.left= TreeNode(2)
    x.left.left= TreeNode(4)
    x.left.right= TreeNode(5)
    x.right= TreeNode(3)
    x.right.left= TreeNode(6)
    x.right.right= TreeNode(7)

    print(soln(x,5))