def soln(A):
    def strSplit(Astx):
        stx1= Astx[:len(Astx)//2]
        if(len(Astx)%2==0):
            return stx1,Astx[len(Astx)//2:][::-1]
        else:
            return stx1,Astx[(len(Astx)//2)+1:][::-1]
    binRep = []
    counter = 1
    while len(binRep)<A:
        Abin= str(bin(counter)).split('b')[1]
        Astr1, Astr2 = strSplit(Abin)
        if(Astr1==Astr2):
            binRep.append([counter,Abin])
        counter += 1
    return binRep[-1][0]

if __name__ == "__main__":
    print(soln(9))