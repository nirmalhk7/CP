

def soln(A):
    import heapq
    r= [i for i in range(A)]
    heapq.heapify(r)
    return r


if __name__ == "__main__":
    print(soln(4))