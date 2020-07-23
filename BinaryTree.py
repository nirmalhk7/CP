class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def printBT(head):
    if(head!=None):
        print(head.val, end=" ")
        printBT(head.left) 
        printBT(head.right)
    return head

def generate(A):
    # [1,[3,[5,3]],[2,[None,9]]]
    # [1,[3,[5,None]],[2,[None,None]]]
    return TreeNode(A)