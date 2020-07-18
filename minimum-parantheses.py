
def soln(A):
    openBrk = 0
    closeBrk= 0
    for i in A:
        openBrk += int(i=='(' or i=="(")
        closeBrk+= int(i==')' or i==")")
    return abs(openBrk-closeBrk)

def soln2(A):
    stx= []
    rx= 0
    for i in A:
        if(i=='('): stx.append('(')
        else:
            if(len(stx)==0):
                rx+=1
            else: stx.pop()
    return rx+len(stx)
if __name__ == "__main__":
    print(soln2("())"))
    print(soln2("((("))
    print(soln2("(())(("))
    print(soln2(")("))