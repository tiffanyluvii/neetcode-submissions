class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        store = [[-1] * n for _ in range(m)]

        def dfs(i:int, j:int) -> int:
            if (i == m - 1 and j == n - 1):
                return 1

            if (i >= m or j >= n):
                return 0

            if (store[i][j] != -1):
                return store[i][j]

            store[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return store[i][j] # allows for previous calls to see what progress has been done so far

        return dfs(0,0)
