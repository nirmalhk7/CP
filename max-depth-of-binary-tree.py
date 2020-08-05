from BinaryTree import *

def soln(A):
    def r(head,hArr=[],height=1):
        if(head!=None):
            r(head.left,hArr,height+1)
            if(not head.left and not head.right):
                hArr.append(height)
            r(head.right,hArr,height+1)
        return hArr
    return max(r(A))

if __name__ == "__main__":
    head=TreeNode(1)
    head.left=TreeNode(2)
    head.left.left=TreeNode(3)
    head.right=TreeNode(4)
    print(soln(head))