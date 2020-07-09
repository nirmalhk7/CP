from LinkedList import *

def soln(A,B):
    temp= A
    arx= []
    while temp:
        arx.append(temp.val)
        temp= temp.next
    arx=arx[-1*B:]+arx[:B+1]
    print(arx,len(arx))
    x=A
    k=0
    while x:
        print(k)
        x.val=arx[k]
        k+= 1
        x=x.next
    return A
if __name__ == "__main__":
    #printList(soln(init([1,2,3,4,5]),2))
    printList(soln(init([23,57,65,90,56,69,77,52,71,74,15,25,41,17,76,95,58,38,29,68,4,89,55,99,13,92,98,62,36,59,54,48,53,12,11,6,2,35,46,39,20,27,44,78,82,67,91,64,97,43,84,83,70,73,79,88,16,1,96,66,80,72,10,19,100,33,75,3,81,24,22,87,63,9,7,40,8,34,101,60,28]),20))