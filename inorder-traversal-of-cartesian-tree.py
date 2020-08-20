from BinaryTree import *

def soln(arr,start=0,end=0):
    if(start>end): return;
    mid= max(arr)-1
    root= TreeNode(arr[mid])
    root.left= soln(arr,start,mid-1)
    root.right= soln(arr,mid+1,end)
    return root

if __name__ == "__main__":
    printBT(soln([1,2,3]))