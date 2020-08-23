import heapq

class DisjointSets:
    class Node:
        def __init__(self,x):
            self.val = x
            self.parent = self
            self.rank = 0

        def __str__(self):
            return str(self.val)

    def findset(self,val):
        if(val.parent!=val):
            val.parent= self.findset(val.parent)
        return val.parent

    def makeset(self,i):
        return self.Node(i)

    def union(self,node1,node2):
        set1= self.findset(node1)
        set2= self.findset(node2)

        if(set1==set2): return False
        if(set1.rank== set2.rank):
            set1.rank+= 1
            set2.parent= set1
        elif(set1.rank>set2.rank): 
            set2.rank+= 1
            set1.parent= set2
            
def soln(A,B):
    nodes=[]
    dsu= DisjointSets()
    for i in range(len(B)):
        nodes.append(dsu.makeset(i))
    while len(B):
        
    sort(B)

        
if __name__ == "__main__":
    A = 4
    B = [   [1, 2, 1],
            [2, 3, 4],
            [1, 4, 3],
            [4, 3, 2],
            [1, 3, 10]  ]
    print(soln(A,B))