class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLen = 0
        maxFreq = 0
        charDict = {}

        for right in range(len(s)):
            charDict[s[right]] = charDict.get(s[right], 0) + 1
            maxFreq = max(maxFreq, charDict[s[right]])

            while (right - left + 1) - maxFreq > k:
                charDict[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen