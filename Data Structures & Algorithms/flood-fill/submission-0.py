class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        colorX = image[sr][sc]
        m, n = len(image), len(image[0])
        if colorX == color:
            return image
        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r, c):
            if image[r][c] == colorX:
                image[r][c] = color
                for dr, dc in dir:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nc < 0 or nr >= m or nc >= n:
                        continue
                    dfs(nr, nc)

        dfs(sr, sc)
        return image
