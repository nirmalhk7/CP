from Tree import *
def buildTree(ino,preo,inStart, inEnd):
    def search(arr,start,end,value):
        for i in range(start,end+1):
            if(arr[i]==value): return i
    if inStart > inEnd:
        return None
    topNode= TreeNode(preo[buildTree.preIndex])
    buildTree.preIndex+= 1
    if inStart == inEnd:
        return topNode
    inIndex= search(ino,inStart,inEnd,topNode.val)
    topNode.left= buildTree(ino,preo,inStart,inIndex-1)
    topNode.right= buildTree(ino,preo,inIndex+1,inEnd)
    return topNode
ino=[2,1,3]
pre=[1,2,3]
buildTree.preIndex=0
printTree(buildTree(ino,pre,0,len(ino)-1))