class Solution:
    
    '''
    Given two strings s and t
    find the shortest substring of s such that every character in t, including dupes, are present in the string.
    else return ""
    '''
    
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0
        res,reslen = [-1,1], float("infinity")
        #characters needed to match
        #create a window, and count characters in T
        window,countT = {},{}
        for c in t:
            countT[c] = countT.get(c,0) + 1   
        have,need = 0, len(countT)

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0)+1
            if c in countT and window[c] == countT[c]:
                have += 1
            
            #attempt to make window smaller from left side until invalid
            while have == need:
                #update res
                if (r-l+1) < reslen:
                    res = [l,r]
                    #set to length of window
                    reslen = (r-l+1)
                #pop left side of window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l += 1
        
        l,r = res
        
        #python slices exclude ending index
        return s[l:r+1] if reslen!= float("infinity") else ""