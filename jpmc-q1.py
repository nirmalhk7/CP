from BinaryTree import *

def soln(root,low,high):
    answer= []
    def recursive(node,valid=True):
        if(node):
            leftValid= recursive(node.left)
            rightValid= recursive(node.right)
            print("NX",node.val,rightValid,leftValid)
            if(leftValid and rightValid):
                answer.append(node.val)
                return True
            if(not (node.left or node.right) and low<=node.val<=high):
                answer.append(node.val)
                return True
        return False
    recursive(root)
    print(answer)





if __name__ == "__main__":
    x= TreeNode(7)
    x.left= TreeNode(5)
    x.right= TreeNode(11)
    x.left.left= TreeNode(2)
    x.left.right= TreeNode(6)
    x.right.left= TreeNode(9)
    x.right.right= TreeNode(15)

    # x.left= TreeNode(1)
    # x.right= TreeNode(11)
    soln(x,5,17)