
def soln(A):
    Alen= len(A)
    lowside= 1
    highside= 1
    for i in range(Alen):
        highside*=A[i]
    for i in range(len(A)):
        highside//=A[i]
        lowside*= A[i]
        print("INIT",A[i])
        A[i]=highside
        print("SETTING",highside,lowside,A[i])
        
    return A
if __name__ == "__main__":
    # print(soln([1,7,3,4]))
    print(soln([1,2,6,5,9]))