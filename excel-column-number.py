def titleToNumber(A):
    val=0
    A=A.lower();
    for i in range(len(A)):
        val+=(ord(A[i])-96)
        if((i+1)!=len(A)):
            val*=26
        
        # if(i+1==len(A)):
        #     val+=ord(A[i])
        # else:
        #     val+=26*(ord(A[i])-96)
    return val

if __name__ == "__main__":
    s="UZ"
    print(titleToNumber(s))