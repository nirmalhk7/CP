def f(a,b):
    if(a==b):
        # strA=bin(a)[2:]
        # count=0
        # for i in range(len(strA)):
        #     if(strA[i]=='1'):
        #         count+=1
        # print("Output",[a,strA],[a,strA],count)
        # return count
        return 0
    else:
        strA=bin(a)[2:]
        strB=bin(b)[2:]
        ACount,BCount=0,0
        for i in range(len(strA)):
            if(strA[i]=='1'):
                ACount+=1
        for i in range(len(strB)):
            if(strB[i]=='1'):
                BCount+=1
        if(ACount>BCount):
            ACount-=BCount
            print("Output",[a,strA],[b,strB],ACount)
            return ACount
        if(ACount==BCount):
            print("Output",[a,strA],[b,strB],ACount)
            return ACount
        else: 
            BCount-=ACount
            print("Output",[a,strA],[b,strB],BCount)
            return BCount

def cntBits(A):
    output=0
    B=A.copy();
    for i in range(len(A)):
        for j in range(len(B)):
            output+=f(A[i],B[j])
    return output % (10**9+7)

if __name__ == "__main__":
    A=[1,3,5]
    A=[ 81, 13, 2, 7, 96 ]
    #print(f(5,3))
    print(cntBits(A))
    print(f(2,7))