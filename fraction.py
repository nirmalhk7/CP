
def soln(A,B):
    def checkRepeats(A):
        hsx={}
    if(A%B==0): return str(A//B)
    sign=""
    if(A<0 ^ B<0):sign="-"
    A=abs(A)
    B=abs(B)
    ans=sign+"0."
    foundRepeat=False
    from collections import OrderedDict
    cache= OrderedDict()
    while True:
        if(A in cache):
            cache[A]="("+str((10*A)//B)
            foundRepeat=True
            break
        if((10*A)%B==0):
            cache[A]=str((10*A)//B)
            break
        cache[A]=str((10*A)//B)
        A=(10*A)%B
    if foundRepeat:
        return ans+"".join(cache.values())+")"
    return ans+"".join(cache.values())
if __name__ == "__main__":
    print(soln(1,2),"0.5")
    print(soln(2,1),"2")
    print(soln(2,3),"0.(6)")
    print(soln(-1,2),"-0.5")