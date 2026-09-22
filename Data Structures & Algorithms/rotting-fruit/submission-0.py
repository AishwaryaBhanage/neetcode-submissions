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

        def bfs(r, c):
            nonlocal fresh

            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or (r, c) in visit
                or grid[r][c] != 1
            ):
                return

            grid[r][c] = 2
            fresh -= 1

            visit.add((r, c))
            q.append((r, c))

        minute = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)

            minute += 1

        return minute if fresh == 0 else -1