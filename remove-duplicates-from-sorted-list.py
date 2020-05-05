class Node:
    # Function to initialize the node object
    def __init__(self, v):
        self.val = v  # Assign value
        self.next = None  # Initialize next as null
  
# Linked List class
class ListNode:
    # Function to initialize the Linked List
    def __init__(self): 
        self.head = None

def itrPtr(A,head=None,grandParent=None):
    if(head==None and grandParent==None):
        head=A
    childPtr=head.next
    if(childPtr and head.val==childPtr.val):
        if(A==head):
            A=A.next
            A=itrPtr(A,head,A)
        else:
            grandParent.next=childPtr
            head=None
            A=itrPtr(A,childPtr,grandParent)
    return A;

def deleteDuplicates(A):
    ParentPtr=A
    itrPtr=A
    grandParent=None
    diffAncesstor=None
    i=0
    while itrPtr.next:
        # print(ParentPtr.val);
        ParentPtr=itrPtr
        childPtr=ParentPtr.next
        if(ParentPtr.val==childPtr.val):
            print("At ",i," Found ",ParentPtr.val,childPtr.val)
            if(grandParent):
                grandParent.next=childPtr
                ParentPtr=None
                print(grandParent.val,"=>",childPtr.val)
            else:
                A=A.next
            pass
        grandParent=ParentPtr
        itrPtr=itrPtr.next
        i+=1
        

    x=A
    print("OUTPUT")

if __name__ == "__main__":
    a=Node(1)
    start=a
    for i in range(20):
        if(i>1):
            for j in range(4):
                a.next=Node(i)
                a=a.next
    x=(itrPtr(start))
    while x:
        print(x.val)
        x=x.next