
def soln(strx):
    def filterString(stx):
        ans=""
        for i in stx:
            if(ord(i) in range(ord('a'),ord('z')+1) or ord(i) in range(ord('A'),ord('Z')+1)):
                ans+=i
        return ans
    strx_arr=strx.split(" ")
    strx_hsx={}
    for i in strx_arr:
        i=filterString(i)
        if(i in strx_hsx):
            strx_hsx[i]+=1
        elif(i.lower() in strx_hsx):
            strx_hsx[i.lower()]+=1
        else:
            strx_hsx[i]=1
        # print(strx_hsx)
    return strx_hsx

if __name__ == "__main__":
    print(soln('Chocolate cake for dinner and pound Cake for dessert'))
    print(soln('Strawberry short cake? Yum!'))
    print(soln('Dessert - mille-feuille cake'))