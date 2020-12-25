#665 Easy Difficulty: Couldnt do. Completed Status
def checkMonotone(nums, index):
    index = max(0, index)
    for i in range(index, len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

def checkPossibility(nums):
    
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            
            bk = nums[i+1]
            nums[i+1] = nums[i]
            if checkMonotone(nums, i):
                return True
            
            nums[i+1] = bk
            nums[i] = nums[i+1]
            
            if not checkMonotone(nums,i-1):
                return False
            else:
                break
            
    return True




print(soln([3, 4, 2, 3]))
# print(soln([3, 4, 2, 3]))
# print(soln([-1,4,2,3]))
# print(soln([4,2,1]))
# print(soln([1,4,3,4]))