class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero_idx = 0
        for idx,value in enumerate(nums):
            if value != 0:
                nums[last_zero_idx],nums[idx] = nums[idx],nums[last_zero_idx]
                last_zero_idx += 1
            