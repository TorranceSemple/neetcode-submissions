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
                print("1")
            elif nums[i] == 0:
                output.append(total)
                print("2")
            elif zeroCount == 1:
                output.append(0)
            else:
                output.append(int(total/nums[i]))
                print("3")

        return output