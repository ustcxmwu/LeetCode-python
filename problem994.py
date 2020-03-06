from typing import List, Tuple


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        while True:
            rotten = list()
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and self.canRotten((i, j), grid):
                        rotten.append((i, j))
            if len(rotten) == 0:
                if self.fresh(grid):
                    return -1
                return minute
            for x, y in rotten:
                grid[x][y] = 2
            minute += 1

    def fresh(self, grid: List[List[int]]):
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    return True
        return False

    def canRotten(self, pos: Tuple[int, int], grid: List[List[int]]):
        four = list()
        x, y = pos
        if x - 1 >= 0:
            four.append(grid[x - 1][y])
        if y + 1 < len(grid[0]):
            four.append(grid[x][y + 1])
        if x + 1 < len(grid):
            four.append(grid[x + 1][y])
        if y - 1 >= 0:
            four.append(grid[x][y - 1])
        if any([True if item == 2 else False for item in four]):
            return True


if __name__ == '__main__':
    # g =[[2,1,1],[0,1,1],[1,0,1]]
    g = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(Solution().orangesRotting(g))
