from BinaryTree import *

def soln(A,B,equal=True):
    if(A!=None and B!=None):
        equal= equal and soln(A.left,B.left);
        equal= equal and soln(A.right,B.right);
        # print("Comparing ",A.val,B.val)
        equal=equal and (A.val==B.val)
    if((A is not None and B is None) or (A is None and B is not None)):
        # print("Missing Node")
        equal= False
    return equal

if __name__ == "__main__":
    t1= TreeNode(1)
    t1.left= TreeNode(2)
    t1.right= TreeNode(3)

    t2= TreeNode(1)
    t2.left= TreeNode(2)
    t2.right= TreeNode(3)
    print(soln(t1,t2))