class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def getNum(lx):
    num=0
    for i in range(len(lx)):
        num=num*10+lx[i]
    return num

def solution(A,B):
    Alist=[]
    Blist=[]
    while A:
        Alist.append(A.val)
        A=A.next
    while B:
        Blist.append(B.val)
        B=B.next
    Alist.reverse()
    Blist.reverse()
    resInt=getNum(Alist)+getNum(Blist)
  #  print(getNum(Alist)+getNum(Blist),Alist,Blist)
    head=ListNode(resInt%10)
    resInt//=10
    prev=head
    while resInt>0:
        node=ListNode(resInt%10)
        prev.next=node
        prev=node
        resInt//=10
    return head
if __name__ == "__main__":
    a=ListNode(2)
    b=ListNode(4)
    c=ListNode(3)
    a.next=b
    b.next=c
    d=ListNode(5)
    e=ListNode(6)
    f=ListNode(4)
    d.next=e
    e.next=f
    
    node=solution(a,d)
    i=0
    while node:
        print("Result ",i,node.val)
        i+=1
        node=node.next
    pass