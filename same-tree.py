from driver_binarytree import *

def soln(head1,head2):
    if(head1==None or head2==None):
        return head1==head2
    # print("Comparing",head1.val,head2.val)
    if(head1.val!=head2.val): return False
    else:
        if(soln(head1.left,head2.left)==False): return False
        if(soln(head1.right,head2.right)==False): return False
    # printTreePreorder(head1)
    return True


if __name__ == "__main__":
    a1= TreeNode(1)
    xx= TreeNode(2)
    a1.left= xx
    xx.right= TreeNode(11)
    a1.right= TreeNode(2)

    a2= TreeNode(1)
    a2.right= TreeNode(2)
    x= TreeNode(2)
    a2.left= x
    x.left=TreeNode(11)
    print(soln(a1,a2))



