# 1711
# Status: Doing

def gm(d):
    count_hash={}
    for i in range(len(d)):
        try:
            count_hash[d[i]]+=1
        except:
            count_hash[d[i]]=1


print(gm([1,3,5,7,9]),4)
print(gm([1,1,1,3,3,3,7]),15)