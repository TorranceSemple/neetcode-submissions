class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for index, value in enumerate(nums):
            # if we are not at the first index and have a repeated number, skip it
            if index > 0 and value == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums)-1
            
            while left < right:
                threeSum = value + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([value, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # skip duplicate lefts
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # skip duplicate rights
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res
                    