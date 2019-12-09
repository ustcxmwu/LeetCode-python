class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        rect1 = [min(A, C), min(B, D), max(A, C), max(B, D)]
        rect2 = [min(E, G), min(F, H), max(E, G), max(F, H)]
        print(rect1)
        print(rect2)


if __name__ == '__main__':
    A = -3
    B = 0
    C = 3
    D = 4
    E = 0
    F = -1
    G = 9
    H = 2
    sol = Solution()
    a = sol.computeArea(A, B, C, D, E, F, G, H)
    print(a)
