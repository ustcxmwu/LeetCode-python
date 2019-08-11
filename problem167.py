import math

class Solution:
    def twoSum(self, numbers, target: int):
        for i in range(numbers[0], math.ceil(target/2) + 1):
            j = target - i
            if i == j:
                if numbers.count(i) >= 2:
                    first = numbers.index(i)
                    return [first+1, numbers.index(i, first+1)+1]
            elif i in numbers and j in numbers:
                return [numbers.index(i)+1, numbers.index(j)+1]



    def twoSum2(self, numbers, target: int):
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if target == numbers[i] + numbers[j]:
                    return [i+1, j+1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
    print(math.ceil(5/2))
    print(5/2)