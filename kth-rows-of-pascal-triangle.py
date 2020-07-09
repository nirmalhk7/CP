def soln(A):
    x=1
    answer=[]
    for k in range(0,A+1):
        answer.append(x)
        x=x*(A-k)//(k+1)
    return answer

if __name__ == "__main__":
    print(soln(3))