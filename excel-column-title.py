
def getInStringForm(out):
    outstring=""
    while len(out):
        outstring+=chr(64+out.pop())
    return outstring

def conT(inp):
    out=[]
    if(inp%26==0):
        out.append(26)
    else:
        out.append(inp%26)
    while(inp>26):
        print(inp,inp//26,inp%26)
        inp=inp//26
        if(inp%26==0):
            out.append(26)
            inp-=1
        else:
            out.append(inp%26)
    print(out)
    return getInStringForm(out)

if __name__ == "__main__":
    print(conT(546))