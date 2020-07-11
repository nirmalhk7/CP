
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def printList(head):
    while head!=None:
        print(head.val,end=" ")
        head=head.next
    print("")

def newNode(val):
    return Node(val,None,None,None)