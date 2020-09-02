from BinaryTree import *


def soln(root,B):
    def find(node):
        if(node==None):
            return False
        if(node.val==B):
            return True
        res1= find(node.left)
        if res1:
            return True
        res2= find(node.right)
        return res2
    array=[]
    def recurse(node,isLeft):
        if(node):
            if(isLeft):
                recurse(node.left,isLeft)
                array.append(node.val)
                recurse(node.right,isLeft)
            else:
                recurse(node.right,isLeft)
                array.append(node.val)
                recurse(node.left,isLeft)
            
    isLeft=find(root.left)
    recurse(root,isLeft)
    print(array)

    pass

def soln2(A,B):
    ans= 0
    def recursive(root,):
        if(root):
            recursive(root.left)
            recursive(root.right)
            ans= max(ans, )
if __name__ == "__main__":
    head= TreeNode(1)
    head.left= TreeNode(2)
    head.right= TreeNode(3)
    head.left.left= TreeNode(4)
    
    head.right.left= TreeNode(5)
    head.right.right= TreeNode(6)
    print(soln(head,4))