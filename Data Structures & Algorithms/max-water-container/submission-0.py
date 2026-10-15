class Solution:
    
    '''
    Given an int array (heights)
    where each value at an index of heights represents the height of that bar. 

    can choose any two bars to form a container, return the max amount of water a container can store
    '''

    def maxArea(self, heights: List[int]) -> int:
        
        l = 0 
        r = len(heights) - 1
        res = 0
        while l < r:
            #find area by getting container width and height
            area = (r - l) * min(heights[l],heights[r])
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r-=1
                l+=1
            res = max(res,area)
        return res