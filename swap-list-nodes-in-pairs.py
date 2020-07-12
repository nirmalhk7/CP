from LinkedList import *
def soln(Al):
    temp= Al
    parent= None
    while temp and temp.next!= None:
        # print("tempval",temp.val)
        A= temp
        B= temp.next
        A.next= B.next
        B.next= A
        # print("Swapping",A.val,B.val)
        if(parent==None):
            Al=B
        if(parent!=None):
            # print("parentval",parent.val)
            parent.next=B
        parent=A
        temp=temp.next
    return Al
if __name__ == "__main__":
    printList(soln(init([1,2,3])))