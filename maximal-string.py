
def soln(A,B):
    Xdef=len(A)
    def r(A,B,X=Xdef):
        if(B>0):
            arrint_A=list(A[Xdef-X:Xdef])
            print(arrint_A,Xdef-X)
            print("B",B,"X",X)
            maxChar, maxCharPosition= '-1',-1
            minChar, minCharPosition= '11',-1
            for i in range(len(arrint_A)):
                if(int(arrint_A[i])>int(maxChar)):
                    maxChar= arrint_A[i]
                    maxCharPosition=i
                if(int(arrint_A[i])<int(minChar)):
                    minChar= arrint_A[i]
                    minCharPosition= i
            if(maxCharPosition>minCharPosition):
                temp= arrint_A[maxCharPosition]
                temp1= maxCharPosition
                arrint_A[maxCharPosition]= arrint_A[minCharPosition]
                maxCharPosition=minCharPosition
                arrint_A[minCharPosition]= temp
                minCharPosition= temp1
            print("DATA",arrint_A,A)
            A=A[0:Xdef-X]+"".join(arrint_A)
            print("FINAL",A)
            A=r(A,B-1,X-1)
            return A
        else:
            return A
    return r(A,B)
        

def soln2(A,B):
    m=A
    def swapStr(A,i,j):
        Alist= list(A)
        temp= Alist[i]
        Alist[i]= Alist[j]
        Alist[j]= temp
        return "".join(Alist)
    def getMax(A=A,B=B,X=m):
        if(B==0):
            return A
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if(A[j]>A[i]):
                    A=swapStr(A,i,j)
                    print(A)
                    if(A>X):
                        X=A
                        getMax(A,B-1,X)
                        A= swapStr(A,i,j)
                        print(A)
    print(getMax())
    # return m

if __name__ == "__main__":
    print(soln2("254",1))
    # print(soln2("254",2))
    # print(soln2("3459",3))
    