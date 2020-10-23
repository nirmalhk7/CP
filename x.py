def calculateMaxSumLength(arr, n, k): 
    ans = 0 # final sum of lengths 
      
    for i in range(n): 
          
        # number of elements in current sub array 
        count = 0
          
        # Variable for checking if k appeared in the sub array 
        flag = 0
          
        # Count the number of elements which are 
        # less than or equal to k  
        while i < n and arr[i] <= k : 
            count = count + 1
            if arr[i] == k: 
                flag = 1
            i = i + 1
              
        # if current element appeared in current 
        # subarray and count to sumLength 
        if flag == 1: 
            print(ans,ans+count)
            ans = ans + count 
              
        # skip the array elements which are greater than k 
        while i < n and arr[i] > k : 
            i = i + 1 
               
    return ans 
      
# Driver Program 
arr = [4,8,5,2,4] 
size = len(arr) 
k = 4
ans = calculateMaxSumLength(arr, size, k) 
print("Max Length ::",ans)