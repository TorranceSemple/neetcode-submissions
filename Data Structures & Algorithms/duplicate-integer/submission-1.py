class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = []
        for num in nums:
            if num not in new_nums:
                new_nums.append(num)
        if len(new_nums) != len(nums):
            return True
        else:
            return False