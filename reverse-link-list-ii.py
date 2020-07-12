from LinkedList import *
def soln(A,B,C):
    temp= A
    lsx= []
    B-=1 
    C-=1
    while temp!=None:
        lsx.append(temp)
        temp=temp.next
    relStartMark= B-1
    lsxlen= len(lsx)
    for i in range(len(lsx)):
        if(i>=B and i<=(C+B)//2):
            target= C-(i-B)
            print("Swapping ",lsx[i].val,lsx[target].val,target)
            temp= lsx[i].val
            lsx[i].val= lsx[target].val
            lsx[target].val= temp
    return lsx[0]
if __name__ == "__main__":
    printList(soln(init([1,2,3,4,5,6,7]),1,3))