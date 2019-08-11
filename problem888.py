import math


class Solution:
    def fairCandySwap1(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        alice_sum = sum(A)
        bob_sum = sum(B)
        Delta = bob_sum - alice_sum
        for elemA in A:
            for elemB in B:
                delta = elemB - elemA
                if 2*delta == Delta:
                    return [elemA, elemB]
        return []


    def fairCandySwap(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        alice_sum = sum(A)
        bob_sum = sum(B)
        Delta = bob_sum - alice_sum
        set_A = set(A)
        set_B = set(B)
        for elemA in set_A:
            test = Delta//2 + elemA
            if test in set_B:
                return [elemA, test]

if __name__ == '__main__':
    for a in range(4):
        print(a)
        print(a//2)