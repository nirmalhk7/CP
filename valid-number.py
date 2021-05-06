
def isStringInteger(y):
    try:
        y_int = int(y)
        return True
    except:
        return False


def soln(s):
    s = s.lower()
    earr = s.split("e")
    eleft = eright = None
    if(len(earr) == 1):
        eleft = earr[0]
    elif(len(earr) == 2):
        eleft, eright = earr
        if('' in [eleft, eright]):
            return False
    else:
        return False
    print(eleft,eright)
    lSeenSign = lIsDecimal = False
    for x in range(len(eleft)):
        if(not isStringInteger(x)):
            if(eleft[x] == "." and not lIsDecimal):
                lIsDecimal = True
            elif(eleft[x] in ["+", "-"] and not lSeenSign):
                lSeenSign = True
            elif(eleft[x] in ["+", "-"] and x != 0):
                return False
            else:
                return False

    eleft_arr = eleft.split(".")

    if(eright):
        rSeenSign = False
        for x in eright:
            if(not isStringInteger(x)):
                if(x in ["+", "-"] and not rSeenSign):
                    rSeenSign = True
                else:
                    return False
    return True


val = ["0", "2", ".1", "0089", "-0.1", "+3.14", "4.", "-.9",
       "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
inv = ["e", ".", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
for i in val:
    print(i, soln(i), True)
for i in inv:
    print(i, soln(i), False)
