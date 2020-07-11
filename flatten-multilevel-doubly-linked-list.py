from LinkedList import *

def soln(head):
    temp= head
    while temp!=None:
        if(temp.child!=None):
            # Set tempNode to next element
            tempNode=temp.next
            # Set child element as next element, and parent as prev of Child
            temp.next=temp.child
            temp.child.prev=temp
            # Remove child element from temp
            temp.child=None
            # Set new temp.next with tempNode
            temp.next.next=tempNode
            tempNode.prev= temp.next
        temp=temp.next
    return head

# def soln2(head,arx=[]):
#     if(head!=None):
#         arx.append(head.val)
#         arx=soln2(head.child,arx)
#         arx=soln2(head.next,arx)
#     return arx

def answer(head):
    if(head): return None
    def soln2(head,arx=[]):
        if(head!=None):
            arx.append(head.val)
            arx=soln2(head.child,arx)
            arx=soln2(head.next,arx)
        return arx
    ansArrForm=soln2(head)
    ansHead=Node(ansArrForm[0],None,None,None)
    temp= ansHead
    for i in range(1,len(ansArrForm)):
        temp.next=Node(ansArrForm[i],temp,None,None)
        temp= temp.next
    return ansHead
if __name__ == "__main__":
    a=newNode(1)
    b=newNode(2)
    c=newNode(3)
    d=newNode(4)
    e=newNode(5)
    a.child=c
    a.next=b
    b.prev=a
    c.next=d
    d.next=e
   # print(soln2(newNode(None)))
    printList(answer(a))