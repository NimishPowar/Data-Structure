class Solution(object):
    def intersection(self, nums1, nums2):

        set1 = set(nums1)
        answer = set()

        for i in range(len(nums2)):
            if nums2[i] in set1:
                answer.add(nums2[i])

        return list(answer)
