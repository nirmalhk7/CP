class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
def printList(head):
    while head!=None:
        print(head.val)
        head=head.next

def init(arx):
    temp = None
    head = None
    for i in arx:
        x=ListNode(i)
        if(head==None): 
            head= x
            
        elif(temp!=None):
            temp.next= x
        temp = x
    return head

def convertToList(A):
    arrForm = []
    while A!=None:
        arrForm.append(A.val)
    return arrForm

if __name__ == "__main__":
    printList(init([1,4,2,3]))