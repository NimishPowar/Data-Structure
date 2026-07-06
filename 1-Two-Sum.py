class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Pair each number with its original index and sort by the number
        indexed_nums = sorted((num, i) for i, num in enumerate(nums))
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum == target:
                # Return the original indices
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
