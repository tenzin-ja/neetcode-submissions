class Solution:
    '''
    Given a string s consisting of characters
    check if the string is valid by matching if 
    every open bracket has a matching closed bracket
    open brackets come first before any closed
    '''
    def isValid(self, s: str) -> bool:

        #idea here is to store all values from s,
        #if we find a closed bracket, there must be a matching
        #open bracket in our stack.
        #if there is, then pop 

        stack = []
        
        #we want to use a hashmap to store the types of 
        #brackets possible, to compare whether they're 
        #open or closed
        hashmap = {')':'(', '}': '{', ']':'['}
        for c in s:
            #if c is one of the keys in the hashmap
            #determine if its stack is empty, and 
            #whether it matches top of stack
            if c in hashmap:
                if stack and hashmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        #return the opposite of state of stack
        #if empty true,else false
        return not stack

            