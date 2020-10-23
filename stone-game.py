def soln(arr):
    def recursive(start=0,end=len(arr)-1,score={True:0,False:0},counter=True):
        if(start==end):
            score[counter]+=arr[start]
            # print("END",score,counter)
            return score[True]>score[False]
        if(arr[start]>arr[end]):
            # print(arr[start],arr[end],'start more')
            score[counter]+=arr[start]
            return recursive(start+1,end,score,not counter)
        else:
            # print(arr[start],arr[end],'end more')
            score[counter]+=arr[end]
            return recursive(start,end-1,score,not counter)
        pass
    return recursive()

if __name__ == "__main__":
    print(soln([5,3,4,5]))