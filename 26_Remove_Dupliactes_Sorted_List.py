class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        i = 1
        n = len(nums)
        while(i < n):
            if nums[i] == nums[idx]:
                i = i + 1
            else:
                idx = idx + 1
                nums[idx] = nums[i]
                i = i + 1        
        return idx+1