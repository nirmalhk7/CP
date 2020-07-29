
def soln(A):
    allOn=True
    for i in A:
        if(i!=1):
            allOn= False
    if(allOn==True): return 0
    else:
        howManyOnFromLeft=0
        for i in A:
            if(i==1):
                howManyOnFromLeft+=1
            else: break
        # print(howManyOnFromLeft)
        return len(A)-howManyOnFromLeft

def soln2(A):
    count = 0
    flag = True
    for bulb in A:
        if bulb == 0 and flag: #this bulb in original state
            count += 1
            flag = False
        elif bulb ==1 and not flag: #this bulb not in orig state, i.e now in off mode
            count += 1
            flag = True
    return count
if __name__ == "__main__":
    # print(soln([1,1,1,1,1]))
    # print(soln([1,0,1,0]))
    print(soln2([0,1,1,0,0,1,0,0,1,0,1,1,0,1,0]))