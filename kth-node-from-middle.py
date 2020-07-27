from LinkedList import *

def soln(head,B):
    arx=[]
    while head!=None:
        arx.append(head.val)
        head= head.next
    positionAns=(len(arx)//2)-B
    # print("PRX",positionAns)
    if(positionAns in range(0,len(arx))):
        return arx[positionAns]
    return -1
if __name__ == "__main__":
    print(soln(init([3,4,7,5,6,16,15,61,16]),3))
    print(soln(init([1,14,6,16,4,10]),2))
    print(soln(init([1,14,6,16,4,10]),10))