
def soln(A):
    stx= []
    for i in A:
        if(i=="("):
            stx.append(i)
        else:
            if(len(stx)!=0):
                stx.pop()
            else:
                return 0
    if len(stx)!=0: return 0
    else: return 1


if __name__ == "__main__":
    # print(soln("(()()))"))
    print(soln("(()((((()("))