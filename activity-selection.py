
def soln(s,e):
    activity=[(s[i],e[i]) for i in range(len(s))]
    activity= sorted(activity,key=lambda x: x[1])
    picking=[]
    for si,ei in activity:
        if(picking)
    # return activity

if __name__ == "__main__":
    start=[5,8,5,1,3,0]
    end=[7,9,9,2,4,6]
    print(soln(start,end))