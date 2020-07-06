class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack=[]

    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):
        if(len(self.stack)!=0):
            self.stack.pop()

    # @return an integer
    def top(self):
        if(len(self.stack)):
            return -1
        else:
            return self.stack[-1:]

    # @return an integer
    def getMin(self):
        if(len(stack)!=0):
            return self.stack.sort()[0]
        else:
            return -1