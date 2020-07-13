class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTreePreorder(head):
    if(head==None):
        return 
    print(head.val,end=" ")
    printTreePreorder(head.left)
    printTreePreorder(head.right)
