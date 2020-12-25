#859 Easy Difficulty: Could do. Completed Status.
def soln(x,y):
    if(len(x)!=len(y)):
        return False
    occurence={}
    for i in x:
        try:
            occurence[i][0]+=1
        except:
            occurence[i]=[1,0]
    for i in y:
        try:
            occurence[i][1]+=1
        except:
            occurence[i]=[0,1]
    for i,j in occurence.values():
        if(i!=j):
            # print("Occurence Change")
            return False
    for i,j in occurence.values():
        if(i>1 and x==y):
            # print("Repeated Change")
            return True
    differenthsx=[]
    for i in range(len(x)):
        if(x[i]!=y[i]):
            differenthsx.append(i)
    return len(differenthsx)==2
    pass

if __name__ == "__main__":
    # print(soln("ba","ab"))
    print(soln("aaaaaaabc","aaaaaaacb"),True)
    print(soln("aaaaaaabc","aaaaaacb"),False)
    print(soln("aa","aa"),True)
    print(soln("a","aa"),False)
    print(soln("","aa"),False)