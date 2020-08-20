from BinaryTree import *

def soln(A):
    def r(head,hArr=[],height=1):
        if(head!=None):
            r(head.left,hArr,height+1)
            if(not head.left and not head.right):
                hArr.append(height)
            r(head.right,hArr,height+1)
        return hArr
    return min(r(A))


if __name__ == "__main__":
    x= TreeNode(12)
    x.left= TreeNode(2)
    print(soln(x))
    pass