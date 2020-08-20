from BinaryTree import *

def soln(A):
    import collections
    root=A
    q= collections.deque()
    q.appendleft(root)
    ans=[]
    while len(q)!=0:
        root=q[-1]
        q.pop()
        while root!=None:
            ans.append(root.val)
            if(root.left):
                q.appendleft(root.left)
            root=root.right
    return ans

if __name__ == "__main__":
    head=TreeNode(1)
    head.right= TreeNode(2)
    head.right.right= TreeNode(3)
    head.right.right.left= TreeNode(6)
    head.left= TreeNode(4)
    head.left.left= TreeNode(8)
    head.left.right= TreeNode(5)
    head.left.right.left= TreeNode(9)
    head.left.right.right= TreeNode(7)
    print(soln(head))