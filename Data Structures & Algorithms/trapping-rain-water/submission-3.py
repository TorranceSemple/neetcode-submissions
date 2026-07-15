class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftMax = 0
        rightMax = 0
        total = 0

        while(l < r):
            if height[l] < height[r]:
                if height[l] > leftMax:
                    leftMax = height[l]
                else:
                    total += leftMax - height[l]
                l += 1
            else:
                if height[r] > rightMax:
                    rightMax = height[r]
                else:
                    total += rightMax - height[r]
                r -= 1
        return total
