class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        answer = None
        max_ele = 0
        for h in hashmap:
            if hashmap[h] > max_ele:
                max_ele = hashmap[h]
                answer = h
        return answer