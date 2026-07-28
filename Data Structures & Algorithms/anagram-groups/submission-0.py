class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in mydict:
                mydict[sorted_word].append(word)
            else:
                mydict[sorted_word] = [word]

        return list(mydict.values())