from LinkedList import *

def soln(head):
    temp= head
    LinkArr = []
    while temp:
        LinkArr.append(temp)
        temp= temp.next
    LinkArr1 = LinkArr[:len(LinkArr)//2]
    LinkArr2 = LinkArr[len(LinkArr)//2:]
    startMark= 0
    endMark= len(LinkArr)-1 
    while startMark<endMark:
        LinkArr[endMark].next=LinkArr[startMark+1]
        LinkArr[startMark+1].next=None
        LinkArr[startMark].next=LinkArr[endMark]
        startMark+=1
        endMark-=1
    return LinkArr[0]
if __name__ == "__main__":
    printList(soln(init([1,2,3,4])))