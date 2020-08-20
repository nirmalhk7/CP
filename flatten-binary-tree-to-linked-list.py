from BinaryTree import *



def soln(x):
    def recursive(head,rock=None):
        if(head!=None):
            print("Going Leftwards",head.left,head.val)
            recursive(head.left,head)
            
            if(head.right!=None and rock):
                rock.left= head.right
        return head
    return recursive(x)
if __name__ == "__main__":
    x= TreeNode(1)
    x.left= TreeNode(2)
    x.right= TreeNode(5)
    x.left.left= TreeNode(3)
    x.left.right= TreeNode(4)
    x.right.right= TreeNode(6)
    printBT(soln(x))
