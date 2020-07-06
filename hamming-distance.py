def soln(x,y):
    xbinstr = str(bin(x)).split('b')[1]
    ybinstr = str(bin(y)).split('b')[1]
    ybinstr='0'*(len(xbinstr)-len(ybinstr))+ybinstr
    xbinstr='0'*(len(ybinstr)-len(xbinstr))+xbinstr
    counter= 0
    for i in range(len(xbinstr)):
        if(xbinstr[i]!=ybinstr[i]):
            counter += 1
    return counter
if __name__ == "__main__":
    print(soln(1,4))