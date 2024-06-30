class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_pointer = 0
        right_pointer = len(nums)-1
        arr = [None]*len(nums)
        res_pointer = right_pointer
        while(left_pointer <= right_pointer):
            left_val = nums[left_pointer]**2
            right_val = nums[right_pointer]**2

            if(right_val>left_val):
                arr[res_pointer] = right_val
                right_pointer -= 1
            else:
                arr[res_pointer] = left_val
                left_pointer += 1
            res_pointer -= 1
        return arr    


        
        