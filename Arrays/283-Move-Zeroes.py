class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        insert = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[insert] = arr[i]
                insert += 1
        for i in range(insert, len(arr)):
            arr[i]=0
        """

        Do not return anything, modify nums in-place instead.
        """