class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        count = 0
        rowLength = len(grid)
        colLength = len(grid[0])

        for rindex, row in enumerate(grid):
            for cindex, item in enumerate(row):
                if item == "1":

                    count += 1

                    self.findOnes(rindex, cindex, rowLength, colLength, grid)
                    

        return count

        

    def findOnes(self, row: int, col: int, rowLength: int, colLength: int, grid: List[List[str]]):

        if row < 0 or row >= rowLength or col < 0 or col >= colLength or grid[row][col] == "0":
            return

        grid[row][col] = "0"

        self.findOnes(row + 1, col, rowLength, colLength, grid)
        
        self.findOnes(row - 1, col, rowLength, colLength, grid)

        self.findOnes(row, col + 1, rowLength, colLength, grid)

        self.findOnes(row, col - 1, rowLength, colLength, grid)


    
