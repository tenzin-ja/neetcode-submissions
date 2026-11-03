class PrefixTree:

    def __init__(self):
        self.trie = {}
        
    #inserts word into the prefix tree
    def insert(self, word: str) -> None:
        
        d = self.trie

        for c in word:
            #if we don't have a character, then we make a new dict
            if c not in d:
                #the character equals a nested dict
                #that'll either store the next char or .
                d[c] = {}
            
            #we set d to the innermost dict, so that we can 
            #continue nesting
            d = d[c]
        
        d['.'] = '.'


    #returns true if the word is in the trie, false otherwise
    def search(self, word: str) -> bool:
        d = self.trie

        for c in word:
            if c not in d:
                return False
            
            d = d[c]
            
        return '.' in d
    #returns true  if there is a previous word that has matching prefix
    #or else false
    def startsWith(self, prefix: str) -> bool:
        
        d = self.trie

        for c in prefix:
            if c not in d:
                return False
            
            d = d[c]
            
        return True