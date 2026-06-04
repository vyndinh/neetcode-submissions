class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIsland = 0
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = "0" # mark as visited

            for dr, dc in dir:
                nr, nc = r+dr, c+dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] == "0":
                    continue
                dfs(nr, nc)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    numIsland += 1
        return numIsland



    