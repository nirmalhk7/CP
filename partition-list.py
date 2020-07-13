from LinkedList import *

def soln(A):
    temp= A
    Aarr= []
    while temp!=None:
        Aarr.append(temp)
        temp=temp.next
    
    return A
if __name__ == "__main__":
    printList(soln(init([1,4,3,2,5,2])))