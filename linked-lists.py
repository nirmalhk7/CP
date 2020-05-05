class Node:
    # Function to initialize the node object
    def __init__(self, v):
        self.val = v  # Assign value
        self.next = None  # Initialize next as null
  
# Linked List class
class ListNode:
    # Function to initialize the Linked List
    def __init__(self): 
        self.head = None

def lPalin(A):
    valStr=[]
    dummyNode=A
    while dummyNode:
        valStr.append(dummyNode.val)
        dummyNode=dummyNode.next
  #  print(valStr)
    front=0
    back=len(valStr)-1
  #  print(front,back)
    while front<=back:
     #   print(valStr[front],valStr[back],"OK")
        if(valStr[front]!=valStr[back]):
      #      print(valStr[front],valStr[back])
            return 0;
        front+=1
        back-=1
    return 1;

if __name__ == "__main__":
    a=Node(5)
    b=Node(4)
    c=Node(3)
    d=Node(4)
    e=Node(5)
    a.next=b
    b.next=c
    c.next=d
    d.next=e
    print(lPalin(a))