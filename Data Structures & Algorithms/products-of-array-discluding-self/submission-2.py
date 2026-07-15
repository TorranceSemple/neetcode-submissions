class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total = 1
        zeroCount = 0
        
        for num in nums:
            if num == 0:
                total = total
                zeroCount += 1
            else:
                total *= num

        for i in range(len(nums)):
            if zeroCount > 1:
                output.append(0)
            elif nums[i] == 0:
                output.append(total)
            elif zeroCount == 1:
                output.append(0)
            else:
                output.append(int(total/nums[i]))

        return output