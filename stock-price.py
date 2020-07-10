def soln(A):
    if(len(A)<2): raise Exception
    # Calculate the max profit
    maxdiff=A[1]-A[0]
    for i in range(len(A)-1):
        maxSell= max(A[i+1:])
        if(maxSell-A[i]>maxdiff): maxdiff=maxSell-A[i]
      #  print("Maxdiff",maxdiff,"Buy",A[i],"Sell",maxSell)
    return maxdiff


if __name__ == "__main__":
    import time
    start=time.time()
    print(soln([10,7,5,8,11,9]))
    print(time.time()-start)