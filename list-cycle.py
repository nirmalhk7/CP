from LinkedList import *

def soln(head):
    hsx={}
    mark= None
    temp= head
    while temp!=None:
        if(temp not in hsx):
            hsx[temp]=True
            temp= temp.next
        else:
            mark=temp
            break
    return mark

if __name__ == "__main__":
    a= ListNode(1)
    a.next= ListNode(2)
    a.next.next= ListNode(3)
    a.next.next.next= ListNode(4)
    a.next.next.next.next= a.next.next
    print(soln(a).val)