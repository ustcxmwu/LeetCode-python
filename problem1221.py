from typing import List

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s) % 2 != 0:
            return 0

        count = 0
        rl = list()
        for letter in s:
            if len(rl) == 0:
                rl.append(letter)
            elif letter == rl[len(rl) - 1]:
                rl.append(letter)
            else:
                rl.pop()
                if len(rl) == 0:
                    count += 1

        return count if len(rl) == 0 else 0



if __name__ == '__main__':
    print(Solution().balancedStringSplit("RLRRLLRLRL"))
