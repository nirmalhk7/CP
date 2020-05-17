def getSubstring(test_str):
    return [int(test_str[i: j]) for i in range(len(test_str)) 
        for j in range(i + 1, len(test_str) + 1)] 

def solution(num):
    numsubstr= getSubstring(str(num))
    prodlist={}
    for xnum in numsubstr:
        xnumcopy=xnum
        prod=1
        while xnumcopy:
            prod*=xnumcopy%10
            xnumcopy//=10
        if(prod in prodlist):
            #print(xnum,prodlist[prod])
            return 0;
        prodlist[prod]=xnum
    return 1
if __name__ == "__main__":
    print(solution(23))