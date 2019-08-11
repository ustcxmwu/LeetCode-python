class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ''.join(e for e in s if e.isalnum()).lower()
        for i in range(len(tmp)//2):
            if tmp[i] != tmp[len(tmp)-1-i]:
                return False
        return True



if __name__ == '__main__':
    pass