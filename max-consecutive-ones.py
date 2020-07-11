def soln(A):
    count=0
    maxCount= 0
    for i in A:
        if(i==1): count+=1
        else: 
            maxCount=max(maxCount,count)
            count=0
    if(count>0 and count>maxCount):
        maxCount=count
    return maxCount
if __name__ == "__main__":
    print(soln([1,1,0,1,1,1]))
    print(soln([1,0,1,1,0,1]))