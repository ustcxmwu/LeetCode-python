from typing import List, Tuple


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and self.communicate((i, j), grid):
                    cnt += 1
        return cnt

    def communicate(self, pos: Tuple[int, int], grid: List[List[int]]) -> bool:
        x, y = pos
        for i in range(len(grid)):
            if i == x:
                continue
            elif grid[i][y] == 1:
                return True
        for j in range(len(grid[0])):
            if j == y:
                continue
            elif grid[x][j] == 1:
                return True
        return False


if __name__ == '__main__':
    # a = [[1, 0], [0, 1]]
    a = [[1, 0, 0, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0]]
    print(Solution().countServers(grid=a))

    a = [1, 1, 1, 2]
    b = [True if item == 1 else False for item in a]
    print(all(b))
