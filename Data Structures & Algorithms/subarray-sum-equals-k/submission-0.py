class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        Given an array of ints, with an int k
        return the total combonations of subarrays whos sum equals to k
        '''

        res = 0
        prefix = {}
        prefix[0] = 1
        total = 0
        for num in nums: 
            total = total + num
            #we want to find the difference between current_total - old = k, finding old
            need = total - k
            if need in prefix:
                res = res + prefix[need]
            prefix[total] = prefix.get(total,0) + 1
        
        return res

