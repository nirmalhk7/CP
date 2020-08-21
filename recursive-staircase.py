

def soln(n,count=0,ans=0):
    if(n>0):
        print("GOING 1",count+1)
        ans+= soln(n-1,count+1)
        print("GOING 2",count+1)
        ans+= soln(n-2,count+1)
        print("GOING 3",count+1)
        ans+= soln(n-3,count+1)
    if(n==0):
        count=0
        return 1
    return 0


if __name__ == "__main__":

    print(soln(5))