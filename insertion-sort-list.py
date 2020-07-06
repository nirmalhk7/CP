from LinkedList import *

def insertionSort(head):
    if(head==None or head.next==None):
        return head
    temp=head.next
    while temp!=None:
        sec_data= temp.val
        t2=head
        found= 0
        while t2!=temp:
            if(t2.val > temp.val and found==0):
                sec_data= t2.val
                t2.val= temp.val
                found= 1
                t2=t2.next
            else:
                if(found==1):
                    xtx= sec_data
                    sec_data= t2.val
                    t2.val= xtx
                t2= t2.next
        t2.val= sec_data
        temp=temp.next
    return head
if __name__ == "__main__":
    printList(insertionSort(init([1,5,4])))