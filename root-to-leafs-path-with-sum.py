from BinaryTree import *

def soln(A,B):
    def r(root,sx,ans=[],curr=[]):
        if(root):
            curr.append(root.val)
            r(root.left,sx-root.val,ans,curr);
            r(root.right,sx-root.val,ans,curr);
            if(not root.left and not root.right and sum(curr)==B):
                ans.append(curr)
                curr=[]
            print("CX",curr,ans,sx,sum(curr))
        return ans
    return r(A,B)

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