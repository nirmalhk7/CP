#306 
# Medium Difficulty
# inCompleted Status.

def soln(num):
    num_int=int(num)
    if(num!=str(num_int)):
        return False
    lsx= list(map(int,num))
    lsx_s=len(lsx)
    if(lsx_s<3):
        return False
    for i in range(2,lsx_s):
        nx=num[i]
        j=i
        while nx!=num[i-1]+num[i-2] and j<lsx_s:
            nx=nx*10+num[j]
            j+=1


print(soln("112358"))