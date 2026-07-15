class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        subStringSet = set()
        l = 0

        for i in range(len(s)):
            while s[i] in subStringSet:
                subStringSet.remove(s[l])
                l += 1
            subStringSet.add(s[i])
            maxLength = max(maxLength, i-l+1)
        return maxLength

