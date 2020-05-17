class Binary:
    def bin_dec(self,A):
        # A: string form.
        A=str(A)
        output=0
        for i in range(len(A)):
            if(A[i]=="1"):
                output +=  2**(len(A)-i-1)
   #             print("OPX",output)
        return output

    def dec_bin(self,A):
        strbin=""
        while A!=0:
            strbin+=str(A%2)
            A//=2
        strbinopx=""
        for i in strbin:
            strbinopx=i+strbinopx
        return strbinopx


def divide(A,B):
    bin = Binary()
    Abinstr = str(bin.dec_bin(A))
    Bbin = int(bin.dec_bin(B))
    print(Abinstr,Bbin)
    output = ""
    consider = Abinstr[0]
    for i in range(len(Abinstr)):
        #consider=Abinstr[:i+1]
        print("Consider ",consider,Abinstr,Bbin,output)
        if(int(consider)>=Bbin):
            output += "1"
            print("Outputting 1")
            consider = str(int(Abinstr)-int(Bbin)) + Abinstr[i+1]
        else:
            output += "0"
            print("Outputting 0")
            consider = Abinstr[:i+2]
        
        
    return int(bin.bin_dec(output))

def divide2(A,B):
    INTMAX=2**32-1
    count = 0
    if(A<B):
        return count
    while A>=0:
        A-=B
        count+=1
    if(count>INTMAX):
        return INTMAX
    return count

if __name__ == "__main__":
    bin = Binary()
 #   print(bin.bin_dec(11))

    print(divide(7,2))
  #  print(bin.bin_dec("011"))
    #print(divide2(5,2))
    pass