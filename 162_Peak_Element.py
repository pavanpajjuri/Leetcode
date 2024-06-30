class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n= len(nums)
        if(n==1): return 0
        if(nums[0] > nums[1]): return 0
        if(nums[n-1]>nums[n-2]): return n-1
        lp = 1
        rp = n-2
        while(lp<=rp):
            i = (lp+rp)//2
            if nums[i-1]<nums[i]>nums[i+1]:
                return i
            elif nums[i-1]>nums[i]:
                rp = i-1
            elif nums[i+1] > nums[i]:
                lp = i+1
        return 1
