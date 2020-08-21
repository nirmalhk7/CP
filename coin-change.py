
def soln(money,denom,index=0):
    if(money == 0): return 1
    if(index >= len(denom)): return 0;
    amountWithCoin= 0
    ways= 0
    while( amountWithCoin <= money ):
        remaining= money- amountWithCoin
        ways+= soln(money,denom,index+1)
        amountWithCoin += denom[index]
    return denom
if __name__ == "__main__":
    print(soln(27,[10,25,5,1]))