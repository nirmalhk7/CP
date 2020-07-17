
def soln(A):
    Aarr= A.split(' ')
    answer=[]
    for i in Aarr:
        if(i!=''):
            answer.append(i)
    answerlen= len(answer)
    for i in range(answerlen//2):
        temp=answer[i]
        answer[i]= answer[answerlen-i-1]
        answer[answerlen-i-1]= temp
    return "".join(answer)

if __name__ == "__main__":
    print(soln("the sky is blue"))
    print(soln("  hello world!  "))
    print(soln("a good   example"))