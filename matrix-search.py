def flatten(input):
    new_list = []
    for i in input:
        for j in i:
            new_list.append(j)
    return new_list

def solution(A,B):
    A= flatten(A)
    for i in A:
        if(i==B):
            return 1
    return 0
if __name__ == "__main__":
    A = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    print(solution(A,16))
    A = [[5,17,100,111],[119,120,127,131]]
    print(solution(A,111))
    A = [[[1,3],[5,7]],[[10,11],[16,20]],[[23,30],[34,50]]]
    print(solution(A,7))