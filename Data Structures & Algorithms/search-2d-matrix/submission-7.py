class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)-1
        length = len(matrix[0])-1

        low = [0,0]
        high = [height, length]

        while low[0] <= high[0] and low[1] <= high[1]:
            mid = [(low[0]+high[0])//2, (low[1]+high[1])//2]
            print(f" val is {matrix[mid[0]][mid[1]]} ")
            print(f" target is {target}, low = {low}, high = {high}, mid = {mid}")
            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] > target:
                if high[1] != 0:
                    high[1] -= 1
                else:
                    high[0] -= 1
                    high[1] = length
            elif matrix[mid[0]][mid[1]] < target:
                if low[1] != length:
                    low[1] += 1
                else:
                    low[0] += 1
                    low[1] = 0
        
        return False
            
        
