class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Given an array nums, and integer k
        return k most frequent elements in the array
        '''
        seen = dict()
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
           seen[num] = seen.get(num,0) + 1
        
        for n,c in seen.items():
            freq[c].append(n)

        for i in range(len(freq) - 1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res