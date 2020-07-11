def soln(A):
    count=0
    for i in A:
        if(len(str(i))%2==0): count+=1
    return count

def soln2(A):
    count=0
    for i in A:
        tempcount=0
        while i>0:
            tempcount+=1
            i//=10
        if(tempcount>2):
            count+= 1
    return count
if __name__ == "__main__":
    import time
    start=time.time()
    print(soln([12,345,2,6,7986]))
    print("----",time.time()-start)
    start=time.time()
    print(soln2([12,345,2,6,7986]))
    print("----",time.time()-start)