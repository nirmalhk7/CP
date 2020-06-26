def solution(A):
    bracketCount = 0
    posnLatest = {'(':None,')':None}
    for i in range(len(A)):
        if(A[i]==')'): 
            bracketCount-=1
            posnLatest[A[i]]=i
        elif(A[i]=='('): 
            bracketCount+=1
            posnLatest[A[i]]=i
    if(bracketCount<0):
        return A[:posnLatest[')']]+A[posnLatest[')']+1:]
    elif(bracketCount>0):
        return A[:posnLatest['(']]+A[posnLatest['(']+1:]
    else:
        return A

def solution2(s):      
    stack,temp=[],[]
    for i in s:
        if i==')':
            while stack and stack[-1]!='(':
                temp.insert(0,stack.pop())
            
            if stack and stack[-1]=='(':
                temp.insert(0,stack.pop())
                temp.append(')')
            
            if temp:
                stack.append("".join(temp))
            temp=[]
        
        else:stack.append(i)
    
    temp=[]
    while stack:
        if stack[-1]!='(' and stack[-1]!=')':
            temp.insert(0,stack.pop())
            
        else:stack.pop()                    
    return "".join(temp)

if __name__ == "__main__":
    print(solution2("lee(t(c)o)de)"))
    print(solution2("a)b(c)d"))