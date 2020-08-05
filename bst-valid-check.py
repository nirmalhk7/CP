class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def soln(head):
    def r(head, isValid=True, headList=[]):
        if(head != None):
            input("Evaluating Node "+str(head.value))
            if(head.left or head.right):
                headList=(headList+[head.value]).copy()
                if(not head.left):
                    print("COMP",head.right.value,head.value,headList)
                    isValid= isValid and max(headList)>= head.right.value >= head.value
                elif(not head.right):
                    print("COMP",head.left.value,head.value,headList)
                    isValid= isValid and min(headList)<= head.left.value <= head.value
                else:
                    print("COMP",head.right.value,head.left.value,headList)
                    isValid= isValid and head.left.value<=head.value<=head.right.value
                # headList.pop()
            isValid= isValid and r(head.left, isValid, headList)
            isValid = isValid and r(head.right, isValid, headList)
            # isValid= isValid and head.left.value<=head.right.value
            # print(head.value,isValid)

        return isValid
    return r(head)

if __name__ == "__main__":
    tree = BinaryTreeNode(50)
    left = tree.insert_left(30)
    right = tree.insert_right(70)
    left.insert_left(10)
    left.insert_right(40)
    right.insert_left(60)
    right.insert_right(80)
    # right.insert_left(80)
    # right.insert_right(60)
    print(soln(tree))
    pass 
