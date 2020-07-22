
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head):
    while head!=None:
        print(head.val,end=" ")
        head=head.next
    print("")

def newNode(val):
    return Node(val,None,None,None)

def init(A):
    Alen= len(A)
    head= None
    master= None
    for i in range(Alen):
        x= ListNode(A[i])
        if(head!=None):
            head.next= x
            head= head.next
        else:
            head= x
            master= x
    return master

