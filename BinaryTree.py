class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def print(self,head):
        if(head!=None):
            print(head.val)
            self.print(head.left) 
            self.print(head.right)
        return head

    def generate(self,A):
        head=TreeNode(4)
        return head