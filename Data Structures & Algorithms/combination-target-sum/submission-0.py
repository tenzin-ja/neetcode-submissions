class Solution:

    '''
    Given an array of ints nums, and a target
    Return a list of all unique combos of nums where the chosen nums add to target

    Same number can be chosen from nums an unlimited number of times
    '''
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        results = []
        
        # 1. Sort ascending so we can prune branches early
        nums.sort()

        def backtrack(remain: int, start: int, path: list[int]):
            # Base Case: Found a combination that hits the target exactly
            if remain == 0:
                results.append(list(path))  # Store a snapshot copy of path
                return

            # Explore all candidate choices starting from index `start`
            for i in range(start, len(nums)):
                num = nums[i]

                # Prune: Since candidates is sorted, if this number exceeds `remain`,
                # every number after it will also exceed `remain`. Stop the loop.
                if num > remain:
                    break

                # 1. CHOOSE
                path.append(num)

                # 2. EXPLORE: Pass `i` (not `i + 1`) to allow reusing `num`
                backtrack(remain - num, i, path)

                # 3. UNCHOOSE: Clean up state before the loop tries the next candidate
                path.pop()

        # Kick off recursion with the full target, start index 0, and an empty path
        backtrack(target, 0, [])
        return results