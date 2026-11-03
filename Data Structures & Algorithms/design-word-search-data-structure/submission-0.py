class WordDictionary:

    def __init__(self):
        self.trie = {}
    
    #create a nested dict
    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]

        #new ending character    
        d['!'] = '!'
    
    #search character by character to determine if word is in the 
    #trie
    def search(self, word: str) -> bool:
        
        d = self.trie

        def dfs(curr, idx):
            #this basically tells us that if the current idx is
            #the length of the word, and the '!' is in curr
            #we have the complete word
            if idx == len(word): return bool('!' in curr)
            

            letter = word[idx]
            if letter != '.':
                if letter not in curr:
                    return False
                else: return dfs(curr[letter], idx + 1)
            else:
                return any(dfs(curr[letter],idx + 1) for letter in curr if letter != '!')
        return dfs(d, 0)