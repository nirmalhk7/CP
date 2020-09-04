
def soln(A):
    original=list(range(min(A),max(A)+1))
    answer=0
    for i in range(len(A)):
        byHowMuch= A[i]-original[i]
        if(0<byHowMuch<=2):
            print(A[i],"Far by",byHowMuch)
            answer+=byHowMuch
        if(byHowMuch>2):
            return "Too chaotic"
    return answer

if __name__ == "__main__":
    A= [1,2,5,3,7,8,6,4]

    print(soln(A))