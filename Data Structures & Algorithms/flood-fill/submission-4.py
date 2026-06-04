class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orgColor = image[sr][sc]
        m, n = len(image), len(image[0])
        if orgColor == color:
            return image
        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r, c, orgColor):
                image[r][c] = color
                for dr, dc in dir:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nc < 0 or nr >= m or nc >= n or image[nr][nc] != orgColor:
                        continue
                    dfs(nr, nc, image[nr][nc])

        dfs(sr, sc, image[sr][sc])
        return image
