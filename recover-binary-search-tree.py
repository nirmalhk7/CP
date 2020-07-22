class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def soln(A):
    stack= []
    result= []
    node=A
    while stack or node:
        if(node):
            stack.append(node)
            node= node.left
        else:
            node= stack.pop()
            result.append(node.val)
            node= node.right
    z= sorted(result)
    for i in range(len(result)):
        if(z[i]!=result[i]):
            return [z[i],result[i]]
        else:
            continue


if __name__ == "__main__":
    a=TreeNode(1)
    a.left= TreeNode(2)
    a.right= TreeNode(3)
    print(soln(a))
    