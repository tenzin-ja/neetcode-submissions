class Solution:
    def isValid(self, s: str) -> bool:
        
        #create stack with list
        stack = list()

        #dict with bracket characters
        mydict = {')':"(" , "}":"{" , "]" : "["}
        #create loop that checks char matches

        for char in s:
            if char in mydict:
                if stack and mydict[char] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False