import math

def soln(A,L):
    answer=[""]*math.ceil(len(' '.join(A))/L)
    strx=""
    marker=0
    for el in A:
        if(len(strx+' '+el)>L):
            print("Cannot add:",strx,len(strx))
            if(A.index(el)!=len(A)-1):
                print("Spaces to add after every letter",L-len(strx)/len(strx.split(' ')))
            answer[marker]=strx
            strx=el
            marker+=1
            print("El",el,"Answer",answer)
            if(A.index(el)==len(A)-1):
                answer[marker]=strx+' '*(L-len(strx))
        else:
            print("Adding",strx,el)
            if(strx==""):
                strx+= el
            else:
                strx+= ' '+el
            if(A.index(el)==len(A)-1):
                answer[marker]=strx+' '*(L-len(strx))
    return answer

def soln2(A,L):
    def processString(X,L):
        print("L",L)
        for i in range(len(X)):
            numOfWords=len(X[i].split())
            if(i==len(X)-1): X[i]=X[i]+' '*(L-len(X[i]))
            else: 
                print("NumSpaces",L-len(X[i])//len(X[i].split()))
        return X
    answer=[""]*math.ceil(len(' '.join(A))/L)
    marker=0
    strx=""
    for i in range(len(A)):
        if(len(strx+' '+A[i])>L and strx!=""):
            print("ARX1",marker)
            answer[marker]=strx
            strx= A[i]
            marker+= 1
            if(marker==len(answer)-1):
                answer[marker]=strx
        else:
            print("ARX2")
            if(strx==""): strx+= A[i]
            else: strx+= ' '+A[i]
            if(marker==len(answer)-1):
                answer[marker]=strx
        print(strx,answer)
    return processString(answer,L)

def soln3(A,B):
    if A==[]: return ""
    jstAns= []
    strx = ""
    A.append("")
    j=0
    for i in A:
        i= i.strip()
        if i=="" or len(i)+len(strx)>=B:
            strx= strx.strip()
            length_str= len(strx) - j + 1
            num_space= j-1
            extra_space= B- length_str
            strx= strx.split()
            if num_space != 0:
                spaces= extra_space // num_space
                remainder_space= extra_space % num_space
                k= 0
                while (remainder_space>0):
                    strx[k]= strx[k]+" "
                    remainder_space -= 1
                    k+= 1
                strx= (" "*spaces).join(strx)
            else:
                spaces= extra_space
                string= " ".join(strx)
                string+= " "*spaces
                remainder_space= 0
            jstAns.append(strx)
            strx= i
            j+= 1
        else:
            strx+= " "+i
            strx= strx.strip()
            j+= 1
    jstAns[-1]= " ".join(jstAns[-1].split())
    jstAns[-1]+= " "*(B-len(jstAns[-1]))
    if(jstAns[0]==""):
        jstAns= jstAns[1:]
    return jstAns

if __name__ == "__main__":
    print(soln3(["This", "is", "an", "example", "of", "text", "justification."],16))
    print(soln3(["What","must","be","shall","be."],12))
    