
def soln(A):
    def getFibonacci(target):
        ans=[1,1]
        f1,f2=ans[0],ans[1]
        while(f1+f2<target):
            f3= f1+f2
            ans.append(f3)
            f1= f2
            f2= f3
        return ans
    numberList= getFibonacci(A)
    print(numberList)
    # from collections import deque
    # q=deque([[1,0,1]])
    # minAttempts=100000000000000000000
    # while q:
    #     element, index, count= q.popleft()
    #     for i in range(index+1,len(numberList)):
    #         if(element+numberList[i]<A):
    #             print(element,"+",numberList[i],"satisfies")
    #             q.append([element+numberList[i],i,count+1])
    #         elif(element+numberList[i]==A):
    #             minAttempts= min(count,minAttempts)
    # print(minAttempts)

def soln2(A):
    from collections import deque
    
if __name__ == "__main__":
    print(soln(4))