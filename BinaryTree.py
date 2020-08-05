class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def printBT(head):
    if(head!=None):
        print(head.val)
        printBT(head.left)
        printBT(head.right)
    return head