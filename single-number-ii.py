def solution(A):
    ones = 0
    twos = 0
    for i in A:
        twos = twos | (i & ones)
        ones = ones ^ i
        mask = ~ (ones & twos)
        ones &= mask
        twos &= mask
    return ones;

if __name__ == "__main__":
    print(solution([1,1,1,2]))    