from LinkedList import *

def soln(A,B):
    nodeAr, temp=[], A
    while temp!=None:
        nodeAr.append(temp.val)
        temp=temp.next

    ans, altYes,nodeArlen=[], True, len(nodeAr)
    for i in range(0,nodeArlen,B):
        if(altYes):
            ans+=nodeAr[i:i+B][::-1]
        else:
            ans+=nodeAr[i:i+B]
        altYes= not altYes

    ansLen, parent=len(ans), ListNode(ans[0])
    for i in range(ansLen):
        ans[i]=ListNode(ans[i])
        parent.next=ans[i]
        parent=ans[i]
    return ans[0]


        
if __name__ == "__main__":
    printList(soln(init(['3', '4', '7', '5', '6', '6', '15', '61', '16']),3))