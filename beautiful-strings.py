
def soln(strx):
    # strx_substr= [strx[i: j] for i in range(len(strx)) 
    substr= []
    for i in range(len(strx)):
        for j in range(i+1,len(strx)+1):
            if(strx[j-1] in strx[i:j-1]):
                break
            else:
                # print("SubstrChar",strx[i:j-1],strx[j-1],substr)
                substr.append(strx[i:j])
    print(substr)
    return substr

print(len(soln("dbacd")))