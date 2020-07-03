def solution(A):
    brStack=[]
    for i in A:
        if i!=')': brStack.append(i)
        else:
            flag=True
            print(i,"Flag is ",flag,brStack)
            while len(brStack) and brStack[-1]!='(':
                popElem=brStack.pop()
                if(popElem in ['+','-','*','/']):
                    flag=False
                    print(i,"Flag is ",flag)
                print(i,"Popping",popElem)
            if(flag):
                return True
    return False
if __name__ == "__main__":
    print(solution("((a+b))"),"======================")
    print(solution("(a+b*(c-d))"),"======================")
    print(solution("(a+(b)/c)"))