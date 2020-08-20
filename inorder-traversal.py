from BinaryTree import *

def soln(head,ans=[]):
    if(head!=None):
        soln(head.left,ans)
        ans.append(head.val)
        soln(head.right,ans)
    return ans
if __name__ == "__main__":
    head= TreeNode(1)
    head.right= TreeNode(2)
    head.right.left= TreeNode(3)
    print(soln(head))