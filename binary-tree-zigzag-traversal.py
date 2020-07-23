from BinaryTree import *

def soln(head):
    def r(head,arx={},level=1):
        if(head!=None):
            if level in arx: arx[level].append(head.val)
            else: arx[level]=[head.val]
            arx=r(head.right,arx,level+1)
            arx=r(head.left,arx,level+1)
        return arx

    arx, arr=r(head),[]
    for key,value in arx.items():
        if(key%2!=0 and len(value)):
            value.reverse()
        arr.append(value)
    return arr
            


if __name__ == "__main__":
    a3=TreeNode(3)
    a3.left=TreeNode(9)
    a3.right=TreeNode(20)

    # a3.left.left= TreeNode(2)
    # a3.left.right= TreeNode(12)
    
    a3.right.left= TreeNode(15)
    a3.right.right= TreeNode(7)
    print(soln(a3))
    # printBT(a3)
    print("")