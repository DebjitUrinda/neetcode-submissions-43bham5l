class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_Map = {}
        t_Map = {}

        for c in s:
            if c not in s_Map:
                s_Map[c] = 1
            elif c in s_Map:
                s_Map[c] += 1

        for ch in s:
            if ch not in t_Map:
                t_Map[c] = 1
            elif ch in s_Map:
                t_Map[c] += 1

        for i in s_Map:
            if i in t_Map:
                if s_Map[i] != t_Map[i]:
                    return False

        return True