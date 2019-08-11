class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s)
        t1 = list(t)
        for elem in t1:
            if elem in s1:
                s1.remove(elem)
            else:
                return False
        return False if len(s1) > 0 else True




if __name__ == '__main__':
    a = set('abc')
    b = set('abc')
    print(a)
    print(a==b)
