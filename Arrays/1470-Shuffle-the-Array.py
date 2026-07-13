class Solution(object):
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])     # Add element from the x-half
            result.append(nums[i + n]) # Add element from the y-half
        return result