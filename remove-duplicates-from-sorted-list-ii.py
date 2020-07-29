from LinkedList import *

def soln(head):
    hsx={}
    arx=[]
    while head!=None:
        arx.append(head)
        try:
            hsx[head.val]+=1
        except:
            hsx[head.val]=1
        head= head.next
    ans=None
    ansP= None
    for i in range(len(arx)):
        if(hsx[arx[i].val]==1):
            if(ans==None):
                ansP=ans= arx[i]
            else:
                ansP.next= arx[i]
                ansP= arx[i]
    return ans

def soln2(A):
    temp=None
    p=A
    test=None
    while p.next:
        if(p.val == p.next.val):
            temp= p.next
            test= p.val
            del A
            
if __name__ == "__main__":
    printList(soln(init([1,2,3,3,4,4,5])))
    printList(soln(init([1,1,1,2,3])))