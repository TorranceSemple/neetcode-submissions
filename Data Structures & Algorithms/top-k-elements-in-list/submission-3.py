class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        for num in nums:
            numDict[num] = 1 + numDict.get(num, 0)
        
        returnList = []
        for num, count in numDict.items():
            returnList.append([count, num])
        returnList.sort()

        res = []
        while len(res) < k:
            res.append(returnList.pop()[1])
        return res