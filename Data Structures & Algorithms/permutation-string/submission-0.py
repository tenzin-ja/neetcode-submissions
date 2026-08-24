class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Given two strings s1,s2
        return true if s2 contains a permuation of s1
        else false

        window size = len(s1)
        use hashmap to determine if letters match
        '''

        s1_count = {}
        s2_permutation = {}
        l,r = 0,0
        window_max_size = len(s1)

        #create a dict(hashmap) with the count of chars in s1
        for c in s1:
            s1_count[c] = s1_count.get(c,0) + 1
        
        for r in range(len(s2)):
            
            s2_permutation[s2[r]] = s2_permutation.get(s2[r],0) + 1

            if (r - l + 1) > window_max_size:
                s2_permutation[s2[l]] -= 1
                if s2_permutation[s2[l]] == 0:
                    del s2_permutation[s2[l]]
                l += 1
            
            if s2_permutation == s1_count:
                return True

        return False

                