
def reverse(A):
    a = A
    strbit=""
    while a!=0:
        strbit+=str(a%2)
        a//=2
    zero = ""
    for i in range(32-len(strbit)):
        strbit+="0"
    output = 0
    for i in range(len(strbit)):
        if(strbit[i]=="1"):
            output +=  2**(31-i)
    #    print("Adding "+strbit[i]+"*"+str(2**(31-i)))
  #  print(strbit)
    return output

if __name__ == "__main__":
    print(reverse(3))
#    assert(reverse(3)==3221225472)