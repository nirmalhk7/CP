from BinaryTree import *

def soln(head):
    if(head is None):
        return 0
    result= 0
    q=[]
    q.append(head)
    while(len(q)!=0):
        count= len(q)
        result= max(count, result)
        while count:
            x=TreeNode(q[-1].val,q[-1].left,q[-1].right)
            q.pop()
            if(x.left is not None): q.append(x.left)
            if(x.right is not None): q.append(x.right)
            count-=1
    return result

if __name__ == "__main__":
    head= TreeNode(1)
    head.left= TreeNode(3)
    head.left.left= TreeNode(5)
    head.left.right= TreeNode(3)
    
    head.right= TreeNode(2)
    head.right.right= TreeNode(9)

    print(soln(head))