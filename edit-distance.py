
def soln(A,B):
    def recurse(strA,strB):
        m, n=len(strA), len(strB)
        L=[[None]*(n+1) for i in range(m+1)]
        Lx={}
        for i in range(m+1):
            for j in range(n+1):
                if(i==0): Lx[str(i)+"-"+str(j)]=j
                elif(j==0): Lx[str(i)+"-"+str(j)]=i
                elif()
        return 0
    recurse()

if __name__ == "__main__":
    print(soln("Anshuman","Antihuman"))