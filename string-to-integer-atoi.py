#8 Medium Difficulty

def myAtoi(st):
    num=0
    isNegative=False
    isFraction=False
    for s in st:
        if(s=="-" and not isNegative):
            isNegative=True
        if(s=="." and not isFraction):
            isFraction=True
            num=num+0.0
            continue
        try:
            num=num*10+int(s)
        except:
            if(("a"<=s<="z" or "A"<=s<="Z") and num==0):
                return 0
            continue
        if(not(-2**31<num<(2**31)-1)):
            return -2**31
        print(num,s)
    if(isNegative):
        return -num
    return num

print(myAtoi("4.193 with words"))