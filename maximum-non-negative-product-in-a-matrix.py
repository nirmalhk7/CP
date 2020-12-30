
def soln(grid):
    rc = len(grid)
    cc = len(grid[0])

    def rec(i, j, current):
        if(i < rc and j < cc):
            if(i+1 == rc and j+1 == cc):
                return current*grid[i][j]
            bottom = rec(i+1, j, current*grid[i][j])
            right = rec(i, j+1, current*grid[i][j])
            print([i, j], bottom, right)
            return max(bottom, right)
        return -1
    return rec(0, 0, 1)


grid = [[-1, -2, -3],
        [-2, -3, -3],
        [-3, -3, -2]]
# grid = [[1, -2, 1],
#         [1, -2, 1],
#         [3, -4, 1]]
print(soln(grid))
