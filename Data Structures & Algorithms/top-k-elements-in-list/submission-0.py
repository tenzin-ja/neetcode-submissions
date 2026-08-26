class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Given an array nums, and integer k
        return k most frequent elements in the array
        '''
        seen = dict()
        res = []
        for num in nums:
           seen[num] = seen.get(num,0) + 1

        while k > 0:
            res.append(max(seen,key = seen.get))
            seen.pop(max(seen,key = seen.get))
            k-=1
        
        return res
        
