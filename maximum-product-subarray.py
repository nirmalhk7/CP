# 152
# Medium Difficulty
# Incompleted Status.


def soln(nums):
    current_max_product = nums[0]
    current_min_product = nums[0]
    prev_max_product = nums[0]
    prev_min_product = nums[0]
    global_max_product=nums[0]
    for i in range(1,len(nums)):
        current_max_product = max(prev_max_product * nums[i],prev_min_product * nums[i], nums[i])
        current_min_product = min(prev_max_product * nums[i],prev_min_product* nums[i], nums[i])
        global_max_product = max(global_max_product,current_max_product)
        prev_min_product = current_min_product
        prev_max_product = current_max_product
    return global_max_product

print(soln([2,3,-2,4]))
print(soln([-2,0,-1]))