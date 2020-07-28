from BinaryTree import *


def soln(inorder, postorder):
    def r():
        

    head = TreeNode(postorder[-1])
    tree_hsx = {}
    for i in range(len(inorder)):
        if(inorder[i] == head.val):
            tree_hsx[head.val] = (inorder[:i], inorder[i+1:])
            break

    return tree_hsx,postorder


def soln2(inorder, postorder):
    def search(arr, strt, end, value):
        i = 0
        for i in range(strt, end + 1):
            if (arr[i] == value):
                break
        return i

    def r(inStrt, inEnd, pIndex):
        if(inStrt > inEnd):
            return None
        node = TreeNode(postorder[pIndex[0]])
        pIndex[0] = -1

        if inStrt == inEnd:
            return node

        iIndex = search(inorder, inStrt, inEnd, node.val)
        node.right = r(iIndex + 1,inEnd, pIndex)
        node.left = r(inStrt,iIndex - 1, pIndex)
        return node
    return r(0,len(inorder)-1,[len(inorder)-1])


if __name__ == "__main__":
    # print(soln([9,3,15,20,7],[9,15,7,20,3]))
    print(soln([1, 9, 6, 3, 15, 20, 7], [1, 6, 9, 7, 20, 3]))