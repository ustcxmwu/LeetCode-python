class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.replace(' ', '')
        if len(str) == 0:
            return 0
        if (str[0] not in ['+', '-'] and not str[0].isdigit()) or \
            (len(str) >= 2 and str[0] in ['+', '-'] and str[1] in ['+', '-']):
            return 0
        flag = 1
        if str[0] == '-':
            flag = -1
            str = str.replace('-', '')
        str = str.replace('+', '')
        nums = []
        for i in range(len(str)):
            if str[i].isdigit():
                nums.append(str[i])
            else:
                break
        if len(nums) > 0 and int(nums[0]) == 0:
            return 0
        power = len(nums) - 1
        ret = 0
        for elem in nums:
            ret += int(elem)*10**power
            power -= 1
        ret = flag*ret
        if ret < -2**31:
            return -2**31
        if ret > 2**31-1:
            return 2**31-1
        return ret




if __name__ == '__main__':
    print('a'.isdigit())
    print(2*10**2)
    sol = Solution()
    print(sol.myAtoi('+0 123'))
