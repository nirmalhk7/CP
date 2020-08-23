
def soln(A):
    def checkOneZero(num):
        while num:
            if(num%10 in [0,1]): return False
            num/=10
        return True
    def r(number,ans=False):e
        ans= r(number*2,ans)
if __name__ == "__main__":
    print(soln(55))