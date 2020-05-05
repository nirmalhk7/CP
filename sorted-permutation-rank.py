from itertools import permutations 

def findRank(A):
    prm=[''.join(p) for p in permutations(A)]
    prm.sort()
    return (prm.index(A)+1)%1000003

if __name__ == "__main__":
    print(findRank("uend"))