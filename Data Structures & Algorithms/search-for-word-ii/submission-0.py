class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        class Trie:

            def __init__(self):
                self.trie = {}
            

            def insert(self,word: str) -> None:
                d = self.trie
                for c in word:
                    if c not in d:
                        d[c] = {}
                    d = d[c]

                d['.'] = '.'
        
        #since this is out of class we don't need the self.
        trie = Trie()

        #inserting all the words into a trie
        for word in words: 
            trie.insert(word)
        

        words = set(words)
        ret_words = set()

        m,n = len(board), len(board[0])

        def backtrack(i, j, st, curr):

            letter = board[i][j]
            st += letter
            if st in words: ret_words.add(st)

            board[i][j] = '#' #mark visited in place
            
            #this loop checks all the boxes around the current one
            #searching for any letters we might need
            for i_off, j_off in [(-1,0) , (0,1), (1,0), (0,-1)]:
                r,c = i + i_off, j+j_off
                if 0 <= r < m and 0 <= c < n and board[r][c] != '#' and board[r][c] in curr:
                    #if we find a letter we need, then we move to that letter
                    #and recurse from it 
                    backtrack(r, c, st, curr[board[r][c]])
                
            #after we're done searching around the letter, we reset its value
            board[i][j] = letter #unmark (backtrack)
            
        #this is to traverse across the board
        #we look for letters that we need, then recurse from that point
        for i in range(m):
            for j in range(n):
                #trie.trie gives us the actual trie
                #trie is just the object, we need the .trie to access the root of our
                #prefix tree
                curr = trie.trie
                if board[i][j] in curr: 
                    backtrack(i, j, '', curr[board[i][j]])
                        
        return list(ret_words)