
def soln(A,n):
    # There must be atleast n units difference between two consecutive items.
    order=[]
    hsx={}
    for i in A:
        try:
            hsx[i]+=1
        except:
            hsx[i]=1
    
    


    # for name in hsx.keys():
    #     hsx[name]-=1
    #     print(name)
    return len(order),hsx
if __name__ == "__main__":
    # print(soln(["A","A","A","B","B","B"],2))
    print(soln(["A","A","A","A","A","A","B","C","D","E","F","G"],2))