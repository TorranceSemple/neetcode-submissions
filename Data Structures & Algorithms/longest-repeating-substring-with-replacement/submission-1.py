class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        charDict = {}
        res = 0
        curr = 0  # max frequency of any single char in the window

        for right in range(len(s)):
            charDict[s[right]] = charDict.get(s[right], 0) + 1
            curr = max(curr, charDict[s[right]])

            while (right - left + 1) - curr > k:
                charDict[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res