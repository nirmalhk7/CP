
def compareVersion(A,B):
    Aarr=[]
    Barr=[]
    temp=0
    for i in range(len(A)):
        if(A[i]!='.'):
            temp=temp*10+int(A[i])
        else:
            Aarr.append(temp)
            temp=0
    Aarr.append(temp)
    temp=0
    for i in range(len(B)):
        if(B[i]!='.'):
            temp=temp*10+int(B[i])
        else:
            Barr.append(temp)
            temp=0
    Barr.append(temp)
    if(Aarr[-1]==0):
        Aarr=Aarr[:-1]
    if(Barr[-1]==0):
        Barr=Barr[:-1]
    maxlen=len(Aarr) if len(Aarr)<len(Barr) else len(Barr)
    print(Aarr,Barr,maxlen)
    for i in range(maxlen):
        if(Aarr[i]>Barr[i]):
            print("Aarr["+str(i)+"]="+str(Aarr[i])+"> Barr["+str(i)+"]="+str(Barr[i]))
            return 1
        elif(Aarr[i]<Barr[i]):
            print("Aarr["+str(i)+"]="+str(Aarr[i])+"< Barr["+str(i)+"]="+str(Barr[i]))
            return -1;
        # else:
        #     print("Aarr["+str(i)+"]="+str(Aarr[i])+"= Barr["+str(i)+"]="+str(Barr[i]))
    if(maxlen==len(Aarr) and maxlen==len(Barr)):
        return 0
    else:
        if(len(Aarr)==maxlen): 
            return -1
        else: return 1
if __name__ == "__main__":
    print(compareVersion('1.0','1'))