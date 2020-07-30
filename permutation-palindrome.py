
def soln(strx):
    strx_hsx={}
    for i in strx:
        try:
            strx_hsx[i]+=1
        except:
            strx_hsx[i]=1
    oddNumCharCount= 0
    for i in strx_hsx.keys():
        if(strx_hsx[i]%2!=0): oddNumCharCount+=1
    return oddNumCharCount<=1

if __name__ == "__main__":
    print(soln("civic"),True)
    print(soln("ivicc"),True)
    print(soln("civil"),False)
    print(soln("livci"),False)
    print(soln("mmaaa"),True)