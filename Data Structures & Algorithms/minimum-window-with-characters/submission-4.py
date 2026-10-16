class Solution:

    '''
    Given two strings, s and t return shortest substring of t in s
    else return false
    '''

    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        l = 0
        window, sublen = [-1,1], float("infinity")
        countS, countT = {}, {}

        for c in t: 
            countT[c] = countT.get(c,0) + 1
        have,need = 0, len(countT)
        
        for r in range(len(s)):
            
            c = s[r]
            countS[c] = countS.get(c,0) + 1

            if c in countT and countS[c] == countT[c]:
                have += 1
            
            #continue looping until we find the smallest window from current one
            while have == need:
                if (r - l + 1) < sublen:
                    sublen = r-l+1
                    window = [l,r]

                #shrink the window from the left side
                countS[s[l]] -= 1

                #check if left char matches in countT and if have and need stay the same             
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        l,r = window

        return s[l:r+1] if sublen != float("infinity") else ""
        