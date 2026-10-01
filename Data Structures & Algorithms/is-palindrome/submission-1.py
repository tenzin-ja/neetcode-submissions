class Solution:

    '''
    Pharse is considred a palindrome if hrase reads the same forward and backward.

    Given a string s, return true if it is a palindrome, or false
    '''
    def isPalindrome(self, s: str) -> bool:

        #First clean the phrase
        cleaned_string = "".join(filter(str.isalnum,s))
        cleaned_string = cleaned_string.lower()
        left = 0
        right = len(cleaned_string)-1
        
        while left < right:

            if cleaned_string[left] == cleaned_string[right]:
        
                left +=1 
                right -= 1
            else:
                print(cleaned_string)
                print(left,right)
                return False
        
        return True