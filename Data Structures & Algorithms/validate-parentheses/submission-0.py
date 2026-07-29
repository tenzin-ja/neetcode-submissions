class Solution:
    def isValid(self, s: str) -> bool:

        #Iterate through string, accept if bracket is open
       # if closed, then compare with most recent char, if char match, then pop 
        #if doesn't match, then return false, if does match continue
        #return true if stack is empty 

        stack = list()
        mydict = {")": "(", "]": "[", "}" :"{"}

        for char in s:
            
            if char in mydict:
                if stack and mydict[char] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)
        return True if not stack else False