from LinkedList import *

def soln(A,B):
    temp= A
    parent= None
    Aarr= []
    while temp!=None:
        Aarr.append(temp.val)
        temp= temp.next
    Aarrlen= len(Aarr)
    answer= []
    for i in range(Aarrlen):
        if(Aarr[i]!=B): 
            answer.append(Aarr[i])
    # print(answer)
    anshead= None
    master= None
    for i in answer:
        x= ListNode(i)
        if(anshead==None): 
            anshead= x
            master= x
        else: 
            anshead.next= x
            anshead= x
    return master
if __name__ == "__main__":
    printList(soln(init([1,2,6,3,4,5,1,6]),1))
    printList(soln(init([1,1]),1))