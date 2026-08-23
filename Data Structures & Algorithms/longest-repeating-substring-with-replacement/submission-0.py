class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Given a string s consising of uppercase letters
        Given an int k
        Return longest substring that only contains one distinct character
        '''

        l,r = 0,0
        maxf = 0

        max_length = 0
        char_amount = {}

        for r in range(len(s)):
            char_amount[s[r]] = 1 + char_amount.get(s[r],0)
            maxf = max(maxf,char_amount.get(s[r]))
            if (r - l + 1) - maxf > k:
                char_amount[s[l]] -= 1
                l = l + 1
            max_length = max(max_length, r - l + 1)
        return max_length