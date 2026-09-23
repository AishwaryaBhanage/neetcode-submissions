class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])

    # Find the unsurrounded region("O in borders") and replace with "T"
        def dfs(r,c):
            if (r<0 or r==ROWS or c<0 or c==COLS or
                board[r][c] != 'O'):
                return
            
            board[r][c] = "T"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

    # Capture those unsurroudned region
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in (0, ROWS-1) or c in (0, COLS-1)):
                    dfs(r,c)

    # Find the surrounded region "O" in middle and replace with X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
    
    # Get the unsurrounded regiion "T" and replace back with "O".
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        


