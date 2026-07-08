class Solution(object):
    def longestConsecutive(self, nums):
        if nums is None:
            return 0
        
        nums_set = set(nums)
        longest = 0
        
        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                count = 1
                
                while current + 1 in nums_set:
                    current += 1
                    count += 1
                    
                if count > longest:
                    longest = count
                    
    
        return longest