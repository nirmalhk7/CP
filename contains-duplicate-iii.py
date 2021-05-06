from collections import deque


def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    item_hsx={}
    for x in numbers:
        if(x in item_hsx):
            return x,x
        item_hsx[x]=1
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m1,m2


def soln(nums, k, t):
    k += 1
    window = deque(nums[:k])
    sv, ssv= second_smallest(window)
    if(abs(sv-ssv) <= t):
        return True
    # print(window,sv,ssv)
    for i in range(k, len(nums)):
        window.append(nums[i])
        window.popleft()
        sv, ssv= second_smallest(window)
        if(abs(sv-ssv) <= t):
            return True
        # print(window, sv,ssv, i, nums[i])
        # winArray.append(list(window))
    # for a in winArray:
    return False


print(soln([1, 2, 3, 1], 3, 0))
print(soln([1, 0, 1, 1], 1, 2))
print(soln([1, 5, 9, 1, 5, 9], 2, 3))
print(soln([1,2,2,3,1],3,0))