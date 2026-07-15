class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWaterArea = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                maxBar = 0
                if heights[i] < heights[j]:
                    maxBar = heights[i]
                else:
                    maxBar = heights[j]
                dist = j - i
                if maxBar * dist > maxWaterArea:
                    maxWaterArea = maxBar * dist
        return maxWaterArea
