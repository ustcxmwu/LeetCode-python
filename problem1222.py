from copy import deepcopy
from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        attack_pos = []
        for i, j in zip(reversed(list(range(king[0]))), reversed(list(range(king[1])))):
            if [i, j] in queens:
                attack_pos.append([i, j])
                break
        for i, j in zip(reversed(list(range(king[0]))), list(range(king[1]+1, 8))):
            if [i, j] in queens:
                attack_pos.append([i, j])
                break
        for i, j in zip(list(range(king[0]+1, 8)), reversed(list(range(king[1])))):
            if [i, j] in queens:
                attack_pos.append([i, j])
                break
        for i, j in zip(list(range(king[0]+1, 8)), list(range(king[1]+1, 8))):
            if [i, j] in queens:
                attack_pos.append([i, j])
                break
        for i in reversed(list(range(king[0]))):
            if [i, king[1]] in queens:
                attack_pos.append([i, king[1]])
                break
        for i in range(king[0]+1, 8):
            if [i, king[1]] in queens:
                attack_pos.append([i, king[1]])
                break
        for j in reversed(list(range(king[1]))):
            if [king[0], j] in queens:
                attack_pos.append([king[0], j])
                break
        for j in range(king[1]+1, 8):
            if [king[0], j] in queens:
                attack_pos.append([king[0], j])
                break
        final = []
        for queue in queens:
            if queue in attack_pos:
                final.append(queue)
        return final


if __name__ == '__main__':
    queens = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
    king = [0, 0]
    sol = Solution()
    attack = sol.queensAttacktheKing(queens, king)
    print(attack)
