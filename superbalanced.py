class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def soln(head):
    def r(head,ans=[],heightMarker=1):
        if(head!=None):
            r(head.left,ans,heightMarker+1)
            if(head.left==None and head.right==None):
                ans.append(heightMarker)
            # print(head.value,ans,heightMarker+1)
            r(head.right,ans,heightMarker+1)
        return ans
    heightList= sorted(r(head))
    # print(heightList)
    # superbalanced= True
    return abs(heightList[0]-heightList[-1])<=1

if __name__ == "__main__":
    h=BinaryTreeNode(1)
    (h.insert_left(2)).insert_left(6)
    hr=h.insert_right(3)
    hr.insert_left(4)
    ((hr.insert_right(5)).insert_right(7)).insert_left(8)
    print(soln(h))
