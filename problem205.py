class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        for i in range(len(s)):
            if s[i] not in s_map.keys():
                if t[i] in s_map.values():
                    return False
                else:
                    s_map[s[i]]=t[i]
            else:
                if s_map[s[i]] != t[i]:
                    return False
        return True



if __name__=='__main__':
