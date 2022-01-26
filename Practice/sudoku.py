import numpy as np

grid = [
 [0, 0, 0, 0, 1, 5, 0, 7, 0],
 [0, 3, 4, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 7, 0, 0, 4, 2, 0],
 [9, 4, 0, 1, 5, 7, 8, 3, 0],
 [0, 2, 8, 0, 0, 0, 7, 0, 0],
 [0, 0, 0, 0, 0, 4, 1, 0, 0],
 [0, 0, 0, 0, 0, 2, 0, 0, 0],
 [4, 0, 9, 8, 0, 0, 0, 5, 0],
 [2, 0, 7, 0, 0, 9, 0, 0, 3]
 ]

 
grid = [
 [3, 5, 0, 0, 7, 0, 0, 0, 0],
 [6, 0, 0, 1, 9, 5, 0, 0, 0],
 [0, 9, 8, 0, 0, 0, 0, 6, 0],
 [8, 0, 0, 0, 6, 0, 0, 0, 3],
 [4, 0, 0, 8, 0, 3, 0, 0, 1],
 [7, 0, 0, 0, 2, 0, 0, 0, 6],
 [0, 6, 0, 0, 0, 0, 2, 8, 0],
 [0, 0, 0, 4, 1, 9, 0, 0, 5],
 [0, 0, 0, 0, 8, 0, 0, 7, 9]
 ]


grid = np.array(grid)

def isPossible(x,y,n):
    ### return boolean n allowed in pos (x , y) ###
    global grid
    if n in grid[y] or n in grid[:,x]:
        return False
    subGridCol = (x // 3)*3
    subGridRow = (y // 3)*3
    for i in range(3):
       for j in range(3):
            if grid[i+subGridRow][j+subGridCol] == n:
                return False
    return True

def solve():
    global grid
    for x in range(9):
        for y in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if isPossible(x,y,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))

print(np.matrix(grid))
solve()