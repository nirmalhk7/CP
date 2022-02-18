# 1488
# Status: Couldnt Do
from collections import deque, defaultdict
import heapq


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        n = len(rains)

        m = defaultdict(deque)
        inq = defaultdict(int)
        for i, x in enumerate(rains):
            m[x].append(i)

        h = []
        res = [-1]*n

        for i, x in enumerate(rains):
            if x:
                if inq[x]:
                    return []

                if len(m[x]) > 1:
                    m[x].popleft()
                    heapq.heappush(h, (m[x][0], x))
                    inq[x] = 1
            else:
                if h:
                    a = heapq.heappop(h)[1]
                    res[i] = a
                    inq[a] = 0
                else:
                    res[i] = 1
        if h:
            return []

        return res


def af(rains):
    ans = []
    zero_indexes = []
    occurences = {}
    for i in range(len(rains)):
        if(rains[i] > 0):
            ans.append(-1)
            # print(occurences,rains[i])
            if(rains[i] in occurences):
                if(len(zero_indexes) == 0):
                    # print("NO ZERO ANSWER")
                    return []
                prev_zero_index = zero_indexes.pop()
                # print("PREVZ",prev_zero_index)
                if(occurences[rains[i]] > prev_zero_index):
                    # print("ZERO LOCHA, ANSWER")
                    zero_indexes.append(prev_zero_index)
                    return []
                else:
                    ans[prev_zero_index] = rains[i]
                    del occurences[rains[i]]
            else:
                # print("New occurence rains[{}]={}".format(i,rains[i]))
                occurences[rains[i]] = i
        else:
            ans.append(1)
            # print("Found a zero at",i)
            zero_indexes.append(i)
    # print("ANSWER")
    return ans


print(af([1, 2, 3, 4]), [-1, -1, -1, -1])
print(af([1, 2, 0, 0, 2, 1]), [-1, -1, 2, 1, -1, -1])
print(af([1, 2, 0, 1, 2]), [])
print(af([69, 0, 0, 0, 69]), [-1, 69, 'x', 'y', -1])
print(af([10, 20, 20]), [])
print(af([2, 0, 2, 0, 1, 1]), [])
print(af([1, 0, 2, 3, 0, 1, 2]), [-1, 1, -1, -1, 2, -1, -1])
