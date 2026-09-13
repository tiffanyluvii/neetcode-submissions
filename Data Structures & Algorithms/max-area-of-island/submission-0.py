class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxArea = 0
        maxRow = len(grid)
        maxCol = len(grid[0])

        for rIndex in range(len(grid)):
            for cIndex in range(len(grid[0])):
                size = self.findArea(rIndex, cIndex, maxRow, maxCol, grid)
                if size > maxArea:
                    maxArea = size
        return maxArea

    def findArea(self, rIndex: int, cIndex: int, maxRow: int, maxCol: int, grid: List[List[int]]) -> int:
        if (rIndex < 0 or rIndex >= maxRow or cIndex < 0 or cIndex >= maxCol or grid[rIndex][cIndex] == 0):
            return 0
        
        grid[rIndex][cIndex] = 0

        return 1 + self.findArea(rIndex + 1, cIndex, maxRow, maxCol, grid) + self.findArea(rIndex - 1, cIndex, maxRow, maxCol, grid) + self.findArea(rIndex, cIndex + 1, maxRow, maxCol, grid) + self.findArea(rIndex, cIndex - 1, maxRow, maxCol, grid)
