class Solution:
    #given a 2d grid board, and a string word,
    #return true if the word is present, otherwirse
    #return false
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        #rows are the length of number of inner arrays
        #cols are the length of number of nums in each inner array
        ROWS, COLS = len(board), len(board[0])

        #index is to track where we are at in the target word
        def dfs(r,c,i):
            
            #checking boundaries or char matches
            if not (0<= r < ROWS and 0 <= c < COLS) or board[r][c] != word[i]:
                return False
            

            if i == len(word) - 1:
                return True
            
            temp,board[r][c] = board[r][c], '#'

            found = any(
                dfs(r+dr, c+dc, i+1)
                for dr,dc in ((1,0), (-1,0), (0,1), (0,-1))
            )
            board[r][c] = temp
            
            return found 

        # Try starting a path from every cell in the matrix
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        
        return False

            