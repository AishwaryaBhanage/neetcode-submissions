class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visit.add((r, c))
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [[1,0],[-1,0], [0,1],[0,-1]]
        minute = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr , c + dc
                    if (row <0 or row == len(grid) 
                        or col < 0 or col == len(grid[0]) or
                        grid[row][col]!= 1):
                        continue

                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1

            minute += 1

        return minute if fresh == 0 else -1

