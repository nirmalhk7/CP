from BinaryTree import *

def soln(A,B,C):
    def getPath(root,target,ans):
            if(not root):
                return False
            ans.append(root.val)
            if(root.val==target):
                return True
            if((root.left!=None and getPath(root.left,target,ans)) or (root.right!=None and getPath(root.right,target,ans))):
                return True
            ans.pop()
            return False
    listA, listB=[], []
    Afound, Bfound=getPath(A,B,listA), getPath(A,C,listB)
    result=-1
    for i in range(min(len(listA),len(listB))):
        if(listA[i]!=listB[i]):
            result=i-1
            break
    # print(listA,listB)
    return listA[result]
    pass
if __name__ == "__main__":
    head= TreeNode(3)
    head.left= TreeNode(5)
    head.right= TreeNode(1)
    head.left.left= TreeNode(6)
    head.left.right= TreeNode(2)
    head.left.right.left= TreeNode(7)
    head.left.right.right= TreeNode(4)
    
    head.right= TreeNode(1)
    head.right.left= TreeNode(0)
    head.right.right= TreeNode(8)

    print(soln(head,5,1))
    pass