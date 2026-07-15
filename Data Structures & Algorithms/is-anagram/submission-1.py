class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        new_s = sorted(s)
        new_t = sorted(t)
        for i in range(max(len(new_s),len(new_t))):
            if new_s[i] != new_t[i]:
                return False
        return True