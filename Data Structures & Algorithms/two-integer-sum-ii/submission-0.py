class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        sorted array 
        
        return indicies of two numbers, [i,i2] 
        i< i2 and i+i2 = target and i != i2
        '''

        l = 0
        r = len(numbers) - 1

        while l < r: 
            sum = numbers[l]+ numbers[r]                

            if sum == target and l != r: 
                return [l+1,r+1]
                l += 1
                r -= 1
            elif sum > target: 
                r -= 1
            else:
                l+=1 
            
