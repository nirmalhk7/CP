from LinkedList import *

def sorted(A):
    itrx = A
    listA = []
    while itrx!=None:
        listA.append(itrx.val)
        itrx = itrx.next
    listA.sort()
    head = None
    temp = None
    for i in listA:
        x=ListNode(i)
        if(head==None): 
            head= x
            
        elif(temp!=None):
            temp.next= x
        temp = x
    return head

if __name__ == "__main__":
    x=init([1,4,2,3])
    printList(sorted(x))