class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        '''
        Given an array of ints: nums
        return length of the longest consecuritive sequence of elements 

        consec sequence: elements in which element is 1 greater then the prev elements, exam 1,2,3 etc
        '''

        #create length result
        res = 0
        #store the current longest sequence
        seen = set(nums)

        for n in seen: 
    
            if n-1 not in seen:
                length = 1
                current = n
                while current + 1 in seen:      
                    current += 1 
                    length +=1 
                
                res = max(length,res)
        return res