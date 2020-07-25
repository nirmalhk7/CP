
def soln(n):
    def decTObin(decx):
        return bin(decx).split('b')[1]
    def binTOdec(binx):
        return int(binx,2)
    def nextGRAY(binx):
        pass
    def r(n,ansBIN="0",ansARR=[]):
        if(len(ansBIN)!=n):
            ansARR.append(binTOdec(ansBIN))
            # Get next gray code

        return ansBIN,ansARR
            
    def genGRAYlist(n):
        anslist= []
        anslist.append("0")
        anslist.append("1")
        i,j= 2,0
        while True:
            if i>=1<<n: break
            for j in range(i-1,-1,-1): anslist.append(anslist[j])
            for j in range(i): anslist[j]="0"+anslist[j]
            for j in range(i,2*i): anslist[j]="1"+anslist[j]
            i = i<<1
        return anslist
    ans=genGRAYlist(n)
    for i in range(len(ans)):
        ans[i]=binTOdec(ans[i])

    return ans

if __name__ == "__main__":
    print(soln(4))