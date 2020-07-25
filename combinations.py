
def soln(A,B):
    def rx(A,B,r=[],s=[],ind=0):
        if(len(s)==B):
            l=[]
            l+=s
            r.append(l)
            return
        for i in range(ind,len(A)):
            s.append(A[i])
            rx(A,B,r,s,i+1)
            s.pop()
        return s
    return rx([i+1 for i in range(A)],B)
if __name__ == "__main__":
    print(soln(4,2))