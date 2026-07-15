class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWaterArea = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            dist = right - left
            area = min(heights[left], heights[right]) * dist
            maxWaterArea = max(maxWaterArea, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxWaterArea

    # def maxArea(self, heights: List[int]) -> int:
    #     maxWaterArea = 0
    #     for i in range(len(heights)):
    #         for j in range(i+1, len(heights)):
    #             maxBar = 0
    #             if heights[i] < heights[j]:
    #                 maxBar = heights[i]
    #             else:
    #                 maxBar = heights[j]
    #             dist = j - i
    #             if maxBar * dist > maxWaterArea:
    #                 maxWaterArea = maxBar * dist
    #     return maxWaterArea
