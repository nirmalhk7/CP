from LinkedList import *

def Reverse(head,parent=None):
    if(head==None):
        return parent.val
    x= Reverse(head.next,head)
    input()
    head.val= x.val
    print(head.val,x,end=" ")
    if(parent):
        return parent
    else:
        return -999

def soln(head):
    def rec(A,hx=ListNode()):
        if(A.next==None):
            hx= A
            return hx
        rec(A.next,hx)
        p=A
        q=p.next
        q.next=p
        p.next=None
        return hx
    return rec(head)

def soln2(head,parent=None,master=None):
    if(master==None):
        head=master
    if(head==None): 
        return parent
    x=soln2(head.next,head,master)
    input()
    if(parent==None):
        print(head.val,x.val,parent,end=" ")
    else:
        print(head.val,x.val,parent.val,end=" ")
    if(parent!=None):
        return parent
    else:
        return master

if __name__ == "__main__":
    print(soln2(init([1,2,3,4,5])).val)