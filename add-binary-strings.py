def solution(A,B):
    x= str(bin(int(A,2)+int(B,2)))
    return x.split('b')[1]
    
if __name__ == "__main__":
    print(solution("101","11"))