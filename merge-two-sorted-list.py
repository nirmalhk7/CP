class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def solution(A,B):
    Aend = A
    while Aend.next:
        Aend=Aend.next
    Aend.next=B

    nodes = []
    Acopy = A
    while Acopy:
        nodes.append(Acopy)
        Acopy= Acopy.next

    nodes = sorted(nodes, key=lambda node: node.val)
    for i in range(len(nodes[:-1])):
        nodes[i].next=nodes[i+1]
    nodes[-1].next=None
    return nodes[0]
if __name__ == "__main__":
    a=ListNode(5)
    b=ListNode(8)
    c=ListNode(20)
    x=ListNode(4)
    y=ListNode(11)
    z=ListNode(15)
    a.next=b
    b.next=c
    x.next=y
    y.next=z
    ANS = solution(a,x)
    # for i in ANS:
    #     print(i.val)
    while ANS:
        print(ANS.val)

        ANS=ANS.next;