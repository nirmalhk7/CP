def solve(A, B, C):
    hsx={}
    for i in A:
        hsx[i]={"A":1,"B":0,"C":0}
    for i in B:
        try:
            hsx[i]["B"]=1
        except:
            hsx[i]={"A":0,"B":1,"C":0}
    for i in C:
        try:
            hsx[i]["C"]=1
        except:
            hsx[i]={"A":0,"B":0,"C":1}
    ans=[]
    for i in hsx.keys():
        Aval, Bval, Cval = hsx[i]["A"], hsx[i]["B"], hsx[i]["C"]
        if(Aval+Bval+Cval>1):
            ans.append(i)
    return ans

if __name__ == "__main__":
    A= [ 56, 56, 34, 34, 72, 71 ]
    B= [ 56, 56, 34, 34, 72, 71 ]
    C= [ 56, 56, 34, 34, 72, 71 ]
    print(solve(A,B,C))
    pass