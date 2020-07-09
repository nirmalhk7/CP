
def soln(A):
    answer = []
    hans = {}
    target = 0
    for i in range(len(A)):
        hsx = {}
        target = -1*A[i]
        remA = A[:i]+A[i+1:].copy()
        for j in range(len(remA)):
            # If 0-element not in dictionary
            if((target-remA[j]) not in hsx):
                hsx[remA[j]] = remA[j]
            else:
                # 0-element found in Hash Table

                if(A[j]+hsx[target-remA[j]] == target and remA[j] != hsx[target-remA[j]] != -1*target):
                    answer.append([remA[j], hsx[target-remA[j]], -1*target])
                    hans[str(remA[j])+str(hsx[target-remA[j]])+str(-1*target)
                             ] = [remA[j], hsx[target-remA[j]], -1*target]
        print("TGT", target, hsx)
        # print("Checking",A[i],A[j],hsx[A[j]],"ANSWER",answer,"DICT",hsx)
    return hans


def soln2(A):
    answer = {}
    xtarget = 0
    for i in range(len(A)):
        target = xtarget-A[i]
        print("Set target as "+str(xtarget)+"-("+str(A[i])+")="+str(target))
        hsx = {}
        for j in range(i, len(A)):
            if((target-A[j]) not in hsx):
                hsx[A[j]] = A[j]
            elif(A[j]+hsx[target-A[j]]+target == 0 and A[j] != hsx[target-A[j]] != target):
                print("Compared", A[j], hsx[target-A[j]],target)
                answer[str(A[j])+str(hsx[target-A[j]])+str(target)]=[A[j],hsx[target-A[j]],target]
                # answer.append([A[j],hsx[target-A[j]],target])
    return answer

def soln3(A):
    s = []
    for i in range(0, len(A)-1): 
    # Find pair in subarray A[i + 1..n-1]  
    # with sum equal to sum - A[i] 
        curr_sum = 0 - A[i] 
        for j in range(i + 1, len(A)): 
            if (curr_sum - A[j]) in s and A[i]!=A[j]!=curr_sum-A[j]: 
                print("Triplet is", A[i],  
                        ", ", A[j], ", ", curr_sum-A[j]) 
                s.append([A[i],A[j],curr_sum-A[j]])
        return s;

def soln4(nums):
    ht={}
    length=len(nums)
    if(length<3): return []
    nums.sort()
    answer=[]
    for i,n in enumerate(nums):
        ht[n]=i
    for i in range(len(nums)-1):
        if(nums[i]>0): break
        if(i==0 or nums[i]>nums[i-1]):
            for j in range(i+1,length):
                target=-(nums[i]+nums[j])
                if target in ht and ht[target]>j:
                    answer.append([nums[i],nums[j],-(nums[i]+nums[j])])
    return answer

if __name__ == "__main__":
    print(soln4([-1, 0, 1, 2, -1, -4]))
