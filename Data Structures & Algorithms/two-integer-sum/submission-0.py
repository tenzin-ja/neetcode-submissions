class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {} # value, index
        for index, num in enumerate(nums):
            sub = target - num
            if sub in val:
                return [val[sub],index]
            val[num] = index
            print (val)            