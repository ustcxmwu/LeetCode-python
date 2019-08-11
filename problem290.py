class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pa = list(pattern)
        st = str.split(' ')
        if len(pa) != len(st):
            return False
        st_map = {}
        for i in range(0, len(st)):
            if st[i] in st_map.keys():
                if pa[i] != st_map[st[i]]:
                    return False
            else:
                if pa[i] in st_map.values():
                    return False
                st_map[st[i]] = pa[i]
        return True


if __name__=='__main__':
    a = list('abc')
    for i in range(0, 5):
        print(i)
    print(a)