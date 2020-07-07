class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def init(A):
    hashx={}
    root= None
    for e in A:
        x=TreeNode(e[0])
        if(len(e)==4):
            root=x
        x.left= e[1]
        x.right=e[2]
        if(e[1]!=None and e[2]!=None):
            x.left= hashx[x.left]
            x.right=hashx[x.right]
        hashx[e[0]]=x
    return root

def printTree(head):
    if(head):
        print(head.val)
        printTree(head.left)
        printTree(head.right)
    else:
        return