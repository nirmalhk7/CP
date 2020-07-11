from itertools import combinations

def soln(A):
    Alen= len(A)
    answer=[]
    for i in range(2**Alen):
        answer.append([A[j] for j in range(Alen) if(i & 2**j)])
    return answer

if __name__ == "__main__":
    print(soln([1,2,3]))