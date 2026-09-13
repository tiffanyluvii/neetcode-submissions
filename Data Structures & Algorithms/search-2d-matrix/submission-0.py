class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        up = 0
        down = len(matrix) - 1
        targetRow = -1

        while (up <= down):
            mid = up + (down - up) // 2
            
            if (matrix[mid][len(matrix[mid]) - 1] >= target 
            and matrix[mid][0] <= target):
                targetRow = mid
                break
            elif (matrix[mid][len(matrix[mid]) - 1] < target):
                up = mid + 1
            elif (matrix[mid][0] > target):
                down = mid - 1
        
        print(targetRow)
        if (not targetRow == -1):
            return self.binarySearch(matrix[targetRow], target)
        else: 
            return False

    def binarySearch(self, row: List[int], target: int) -> bool:
        left = 0
        right = len(row) - 1

        while (left <= right):
            mid = left + (right - left) // 2
            
            if (row[mid] == target):
                return True
            elif (row[mid] > target):
                right = mid - 1
            elif (row[mid] < target):
                left = mid + 1
        
        return False