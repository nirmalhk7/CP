
def soln(arr):
    arrR=arr[::-1]
    maxNum=arrR[0]
    for i in range(1,len(arrR)):
        maxNum=max(maxNum,arrR[i])
        

if __name__ == "__main__":
    arr=[7,1,5,3,6,4]
    print(soln(arr))