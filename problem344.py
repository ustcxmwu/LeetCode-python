class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            t = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s) - 1 - i] = t


if __name__ == '__main__':
    pass