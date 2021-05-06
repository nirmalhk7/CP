# 941
# Easy Difficulty
# Completed Status.

def soln(arr):
    uphill=True
    for i in range(1,len(arr)):
        if(arr[i]==arr[i-1]):
            return False
        elif(uphill and arr[i]<arr[i-1]):
            if(i==1):
                return False
            uphill=False
        elif(not uphill and arr[i-1]<arr[i]):
            return False
    if(not uphill):
        return True
    return False

print(soln([0,2,3,4,5,2,1,0]),True)
print(soln([0,2,3,3,5,2,1,0]),False)
print(soln([2,1]),False)
print(soln([3,5,5]),False)