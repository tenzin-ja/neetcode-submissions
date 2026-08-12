class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = set()
        length = 0

        for r in range(len(s)):
            if s[r] in longest:
                while s[r] in longest:
                    longest.remove(s[l])
                    l += 1
                longest.add(s[r])
            else:
                longest.add(s[r])
            length = max(length,len(longest))
        return length