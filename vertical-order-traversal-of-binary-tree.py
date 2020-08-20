from BinaryTree import *


def soln(head):
    def r(root,level,ans={}):
        if(root):
            r(root.left,level-1)
            # print("NODE",root.val,level)
            ans[root.val]=level
            r(root.right,level+1)
        return ans
    
    def getLeftMost(root):
        temp=-1
        while root:
            temp+=1
            root=root.left
        return temp

    def filterx(root,hsx):
        ans=[[] for i in range(max(hsx.values())+1)]
        # print(hsx)
        def preorder(root):
            if(root):
                # print("ANS",ans,hsx[root.val])
                ans[hsx[root.val]].append(root.val)
                preorder(root.left)
                preorder(root.right)
            return ans
        return preorder(root)
    lmost= getLeftMost(head)
    return filterx(head,r(head,lmost))



if __name__ == "__main__":
    head= TreeNode(6)
    head.left= TreeNode(3)
    head.right= TreeNode(7)

    head.left.left= TreeNode(2)
    head.left.right= TreeNode(5)
    head.right.right= TreeNode(9)

    print(soln(head))

    # head= TreeNode(1)
    # head.left= TreeNode(2)
    # head.right= TreeNode(3)
    # head.left.left= TreeNode(4)
    # head.left.right= TreeNode(5)
    # print(soln(head))
