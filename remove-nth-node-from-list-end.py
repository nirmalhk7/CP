class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def printAll(headNode):
    while headNode:
        print(headNode.val)
        headNode=headNode.next

def removeNthFromEnd(A,N):
    Acp=A
    if(A):
        nodeCount=1
        while Acp.next:
            nodeCount+=1
            Acp=Acp.next

        if(N>nodeCount):
            popIndex=1
        else:
            popIndex=nodeCount-N+1
        print("PIndex",popIndex," NCount ",nodeCount)
        nodeCount=1
        Acp=A
        if(popIndex==1):
            A=A.next
            return A
        while Acp:
            if(nodeCount+1==popIndex):
                Acp.next=Acp.next.next
            nodeCount+=1
            Acp=Acp.next
        return A


if __name__ == "__main__":
    A=ListNode(1)
    # B=ListNode(2)
    # C=ListNode(3)
    # D=ListNode(4)
    # A.next=B
    # B.next=C
    # C.next=D
    printAll(removeNthFromEnd(A,1))
    
