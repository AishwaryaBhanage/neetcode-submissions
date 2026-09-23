class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c):
            if (r<0 or r==ROWS or c<0 or c==COLS or
                board[r][c] != 'O'):
                return
            
            board[r][c] = "T"
            dfs(r+1, c)
            dfs(r+1, c)
            


