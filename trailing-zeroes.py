
def soln(A):
    Abin= bin(A).split('b')[1][::-1]
    count= 0
    for i in Abin:
        if(i=="1"): break
        else: count+= int(i=="0")
    return count

if __name__ == "__main__":
    # print(soln(18))
    print(soln(8))