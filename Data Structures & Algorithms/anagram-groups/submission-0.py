class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputList = []
        used = [False] * len(strs)  # Track which strings are already grouped
        
        for i in range(len(strs)):
            if used[i]:  # Skip if already in a group
                continue
            
            tempList = [strs[i]]  # Start the group with current string
            used[i] = True
            
            for j in range(i + 1, len(strs)):
                if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                    tempList.append(strs[j])
                    used[j] = True
            
            outputList.append(tempList)  # Add complete group
        
        return outputList