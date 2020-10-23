
def soln(money,denom,index=0,arr_used=[],counter=0,memo={},arr_used_hash={}):
    if(money==0):
        print("FOUND",sorted(arr_used))
        if(str(sorted(arr_used)) not in arr_used_hash):
            arr_used_hash[str(sorted(arr_used))]=True
            return counter+1
        else:
            return counter
    for i in range(len(denom)):
        if(denom[i]<=money):
            print(money,denom[i],counter,memo)
            if(money-denom[i] not in memo):
                counter=memo[money-denom[i]]=soln(money-denom[i],denom,index+1,arr_used+[denom[i]],counter)
            else:
                counter=memo[money-denom[i]]
    return counter
if __name__ == "__main__":
    print(soln(4,[1,2,3]))