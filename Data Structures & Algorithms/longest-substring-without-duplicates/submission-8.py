class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''Given some string 's'
        find the length of the longest substring without dupes'''
        
        l,r = 0,0
        seen = dict()
        max_length = 0 

        while r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                l = 1 + seen.get(s[r])
            seen[s[r]] = r 
            max_length = max(r-l+1,max_length)
            r += 1
        return max_length