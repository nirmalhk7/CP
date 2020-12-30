#605
# Easy Difficulty
# inCompleted Status.


def soln(arr,n):
    zeroArr=[]
    temp=0
    for i in arr:
        if(i==0):
            temp+=1
        else:
            if(temp!=0):
                if(len(zeroArr)==0):
                    zeroArr.append(temp+1)
                else:
                    zeroArr.append(temp)
            temp=0
    if(temp!=0):
        zeroArr.append(temp+1)
    print(zeroArr)
    for i in zeroArr:
        print(n)
        if(i>=3):
            n-=(i-1)//2
    
    return n==0

print(soln([1,0,0,0,1],1),True)
print(soln([1,0,0,0,1],2),False)
print(soln([1,0,0,0,1,0,0],2),True)
print(soln([1,0,0,0,0,0,1],2),True)
print(soln([0,0,1,0,1],1),True)