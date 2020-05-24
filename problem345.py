class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 0:
            return ""
        dic = set(['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U'])
        i = 0
        j = len(s)-1
        ss = list(s)
        while i < j:
            while i < len(s) and ss[i] not in dic:
                i += 1
            while j > 0 and ss[j] not in dic:
                j -= 1
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
    print(sol.reverseVowels('.,'))

