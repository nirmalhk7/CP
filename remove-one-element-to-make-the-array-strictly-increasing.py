# 1909
# Status: Doing

def fun(nums):
    foundTBR=None
    for i in range(1,len(nums)):
        # print(i,nums[i-1],nums[i],foundTBR)
        if(nums[i-1]>=nums[i]):
            if(foundTBR!=None):
                return False
            elif(i==1):
                foundTBR=i-1
            elif(nums[i-2]<nums[i]):
                foundTBR=i-1
            elif(nums[i-2]>=nums[i]):
                if(nums[i-1]<nums[i+1]):
                    foundTBR=i
                else:
                    return False
        print(i,nums[i-1],nums[i],foundTBR)
    return True

print(fun([1,2,10,5,7]))
print(fun([2,3,1,2]))
print(fun([1,1,1]))
print(fun([2,3,1,4,7,6]))
print(fun([2,3,1,2,7,6]))