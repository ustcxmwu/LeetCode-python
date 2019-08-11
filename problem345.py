class Solution:
    def reverseVowels(self, s: str) -> str:
        dic = ['a', 'o', 'e', 'i', 'u']
        i = 0
        j = len(s)-1
        ss = list(s)
        while i < j:
            while ss[i] not in dic:
                i += 1
            while ss[j] not in dic:
                j -= 1
            if i == len(s)-1 or j == 0:
                break
            if i < j:
                t = ss[i]
                ss[i] = ss[j]
                ss[j] = t
                i += 1
                j -= 1
        return ''.join(ss)


if __name__ == '__main__':
    print(len('aaaa'))
    sol = Solution()
    print(sol.reverseVowels('leetcode'))
