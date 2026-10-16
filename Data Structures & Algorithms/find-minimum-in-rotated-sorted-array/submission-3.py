class Solution:
    '''
    Given an array of length n, sorted in ascending order
    its now rotated between 1 to n times. 
    Assuming all elements in the rotated sorted array are unique, return
    the miniumm element of the array
    solution in log n time
    '''
    def findMin(self, nums: List[int]) -> int:
        
        #arbitrary
        res = nums[0]

        #set pointer variables
        l,r = 0, len(nums) - 1

        #loop if left side is smaller than right side
        while l <= r: 
            #if the array is sorted, we can set the new res, and break out
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break

            #compute mid point
            m = (l+r)//2

            #set res to min of mid and res
            res = min(res,nums[m])

            if nums[m] >= nums[l]:
                l = m + 1 
            else:
                r = m - 1
        
        return res