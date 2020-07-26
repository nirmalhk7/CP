
def soln(take_out,dine_in,served):

    take_out.reverse()
    dine_in.reverse()
    for i in range(len(served)):
        # print("finding",served[i],take_out,dine_in)
        if(len(take_out)>0 and served[i]==take_out[-1]): take_out.pop()
        elif(len(dine_in)>0 and served[i]==dine_in[-1]): dine_in.pop()
        else:
            # print("Didnt find",served[i],take_out,dine_in)
            return False
    if(len(take_out)>0 or len(dine_in)): return False
    return True



if __name__ == "__main__":
    # print(soln([1,3,5],[2,4,6],[1,2,4,6,5,3]),False)
    # print(soln([17,8,24],[12,19,2],[17, 8, 12, 19, 24, 2]),True)
    # print(soln([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8]),False)
    print(soln([1, 9], [7, 8], [1, 7, 8]),False)