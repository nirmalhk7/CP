def solution(A):
    charR = ""
    charA = []
    for i in A:
        charR += i
        charA.append(charR)
    ans = ""
    for i in charA:
        dct = {}
        for j in i:
            print(i,j)
            try:
                if(dct[j]==1):
                    ans+=j
            except KeyError:
                dct[j]=1
    return ans

if __name__ == "__main__":
    print(solution("abadbc"))