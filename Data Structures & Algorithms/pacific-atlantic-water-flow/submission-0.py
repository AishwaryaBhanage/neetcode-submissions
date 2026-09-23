class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights) , len(height[0])
        pac, atl = set(), set()

        def dfs(r,c,visits, preHeight):
            if (r < 0 or r == ROWS or c < 0 or c==COLS or (r,c) in visit or 
                heights[r][c] < preHeight):
                return

            dfs(r+1,c, visits, heights[r][c])
            dfs(r+1,c, visits, heights[r][c])
            dfs(r+1,c, visits, heights[r][c])
            dfs(r+1,c, visits, heights[r][c])