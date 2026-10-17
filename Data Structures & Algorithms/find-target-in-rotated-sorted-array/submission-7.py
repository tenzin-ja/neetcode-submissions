class Solution:
    '''
    Given an array of length n thats in ascending but rotated order, find the target int in log n time (binary search)
    '''
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1
        
        #whenever we have a rotated sorted array, we need to find the pivot (minimum value)
        while l < r:
            
            m = (l+r)//2

            if nums[m] > nums[r]: 
                l = m + 1
            else: 
                r = m
            
        min_i = l
        
        # this means were assuming the list is in standard order
        if min_i == 0:
            l,r = 0,len(nums) - 1
        # since the array's left side must be bigger then the min
        # check if target is larger or equal to leftmost, and less then 
        # or equal to number to the left of min
        elif target >= nums[0] and target <= nums[min_i-1]:
            l,r = 0, min_i - 1
        # otherwise, it must be on the right side 
        else:
            l,r = min_i, len(nums)-1
        #we need to set new l and r

        #we want to loop again to check where target is being held
        while l <= r: 
            
            m = (l+r)//2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            #must move by -1 since m if confirmed not target
            else:
                r = m - 1
            
        return -1