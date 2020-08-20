from BinaryTree import *

def soln(head,num):
    def r(root,hsx={}):
        if(root):
            r(root.left,hsx);
            r(root.right,hsx);
            # print("FIND",num,num-root.val)
            if(num-root.val in hsx):
                hsx[root.val]= num-root.val
            else:
                hsx[root.val]= None
        return hsx
    hrx= r(head)
    # print(hrx)
    for i in hrx.values():
        if(i!=None):
            return 1
    return 0


if __name__ == "__main__":
    head= TreeNode(1)
    head.left= TreeNode(2)
    head.right= TreeNode(3)
    head.left.left= TreeNode(4)
    head.left.right= TreeNode(5)
    head.right.left= TreeNode(6)
    head.right.right= TreeNode(7)
    print(soln(head,413))

    head= TreeNode(10)
    head.left= TreeNode(9)
    head.right= TreeNode(20)
    print(soln(head,19))