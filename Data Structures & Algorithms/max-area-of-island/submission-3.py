class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # BFS Solution

        # if not grid:
        #     return 0

        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        # maxarea = 0

        # def bfs(r,c):
        #     q = collections.deque()
        #     q.append((r,c))
        #     visited.add((r,c))
            
        #     area = 1

        #     while q:
        #         row, col =  q.popleft()
        #         directions = [[1,0], [-1,0], [0,1], [0,-1]]

        #         for dr, dc in directions:
        #             r,c  = row + dr, col + dc
        #             if (r in range(rows) and 
        #                 c in range(cols) and 
        #                 grid[r][c] == 1 and
        #                 (r,c) not in visited):
        #                 visited.add((r,c))
        #                 q.append((r,c))
        #                 area += 1
        #     return area

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1 and (r,c) not in visited:
        #             cur_area = bfs(r,c)
        #             maxarea = max(maxarea, cur_area)

        # return maxarea

        
        # DFS Solution

        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r,c):
            
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                grid[r][c] == 0 or (r,c) in visit):
                return 0

            visit.add((r,c))
            return (1 + dfs(r + 1, c)+
                        dfs(r-1, c)+
                        dfs(r, c+1)+
                        dfs(r, c-1))

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))

        return area



