
def soln(A):
    def checkPalindrome(strx):
        return strx==strx[::-1]
    
    # def r(A,startmark=0,endmark=1,subset=[],answer=[]):
    #     print("STM",startmark,"ENM",endmark,A[startmark:endmark])
    #     if(startmark==endmark):
    #         return subset,answer
    #     if(endmark>=len(A)):
    #         return subset,answer
        
    #     if(checkPalindrome(A[startmark:endmark])):
    #         subset.append(A[startmark:endmark])
    #     subset, answer= r(A,endmark=endmark+1,subset=subset,answer=answer)
    #     print("B",subset,answer)
    #     subset, answer= r(A,startmark=startmark+1,subset=subset,answer=answer)
    #     print("C",subset,answer)
    res= []
    def f(s,path=[]):
        if not s:
            res.append(path)
            return
        for i in range(1,len(s)+1):
            if(checkPalindrome(s[:i])): 
                f(s[i:],path+[s[:i]])
        return
    print(res)
    return f(A)

if __name__ == "__main__":
    print(soln("aab"))
