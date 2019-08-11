class Solution:

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = []
        for i in range(numRows):
            row = []
            for j in range(len(s)):
                row.append('')
            arr.append(row)
        i = 0
        j = 0
        direction = ''
        for k in range(len(s)):
            arr[i][j] = s[k]
            if i == 0:
                direction = 'down'
            elif i == numRows - 1:
                direction = 'up'

            if direction is 'up':
                i = i-1
                j = j+1
            elif direction is 'down':
                i = i+1
        ret = []
        for i in range(numRows):
            ret.append(''.join(arr[i]))
        return ''.join(ret)





if __name__ == '__main__':
    sol = Solution()
    print(sol.convert('AB', 1))
