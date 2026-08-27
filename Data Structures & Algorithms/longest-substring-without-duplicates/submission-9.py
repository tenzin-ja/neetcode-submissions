class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        Given a string s, find the length of the longest substring without duplicate char
        '''

        seen = dict()
        max_res = 0
        l = 0

        for r in range(len(s)): 
            if s[r] in seen and seen[s[r]] >= l :
                l = seen.get(s[r]) + 1
            seen[s[r]] = r
            max_res = max(max_res,r-l+1)
        return max_res