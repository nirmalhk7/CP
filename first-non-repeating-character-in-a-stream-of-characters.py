def solution(A):
    charR = ""
    charA = []
    for i in A:
        charR += i
        charA.append(charR)
    ans = ""
    for i in charA:
        dct = {}
        for j in i:
            print(i,j)
            try:
                if(dct[j]==1):
                    ans+=j
            except KeyError:
                dct[j]=1
    return ans

def soln(A):
    def firstNonRepeatingChar(strx):
        hsx= {}
        strxlen= len(strx)
        for i in range(strxlen):
            hsx[strx[i]]=bool(strx[i] not in hsx)
        # print("RRR",sorted(hsx.items(), key=lambda x: x[1],reverse=True)[0])
        if sorted(hsx.items(), key=lambda x: x[1],reverse=True)[0][1]:
            return sorted(hsx.items(), key=lambda x: x[1],reverse=True)[0][0]
        return "#"
    
    # def r(rx,marker=0,ans=""):
    #     if(marker<len(A)):
    #         ans= firstNonRepeatingChar(rx)
    #         print("Evaluating ",rx,ans,marker)
    #         ans+=r(rx+A[marker],marker+1,ans)
    #     return ans

    rx=""
    marker=0
    ans=""
    while marker<len(A):
        rx+=A[marker]
        print("EV",rx,marker,ans,firstNonRepeatingChar(rx))
        ans+= firstNonRepeatingChar(rx)
        marker+=1
    return ans
if __name__ == "__main__":
    # print(soln("iergxwhddh"),"iiiiiiiiii")
    # print(soln("abadbc"),"aabbdd")
    # print(soln("abcabc"),"aaabc#")
    print(soln("gu"),"gg")