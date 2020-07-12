
def soln(A):
    if(A==[]): return []
    Astr="".join(A)
    Arx= Astr.split(" ")
    Arx.reverse()
    return list(" ".join(Arx))
if __name__ == "__main__":
    print(soln(list('yummy is cake bundt chocolate'))==list('chocolate bundt cake is yummy'))