class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        

        nums.sort()
        res = []
        for index,val in enumerate(nums):
            l = index + 1
            r = len(nums) - 1

            if index > 0 and val == nums[index-1]:
                continue 
            while l < r: 
                sum = val + nums[l] + nums[r]
                if sum == 0: 
                    res.append([nums[index],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif sum > 0: 
                    r -= 1
                else:
                    l+=1 
        return res