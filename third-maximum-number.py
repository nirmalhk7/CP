# Easy Difficulty: Could do. Completed Status.
def soln(arr):
    if(len(arr)<3):
        return max(arr)
    max1=max2=max3=-float('inf')

    for i in arr:
        if(max1==max2==max3==float('inf')):
            print('initmax')
            max1=i
        elif(i<max1):
            if(max2<i):
                max3=max2
                max2=i
                print('max2<i')
            elif(max3<i<max2):
                max3=i
                print('max3<i<max2')
        elif(max1<i):
            max3=max2
            max2=max1
            max1=i
            print('max1<i')
        print(max1,max2,max3)
    if(max3==-float('inf')):
        # Meaning return max1 (maximum)
        return max1
    return max3


# print(soln([2,2,3,1]))
print(soln([1,1,2]))
