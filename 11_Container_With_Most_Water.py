class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height)-1
        max_area = 0
        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            min_height = min(height[left_pointer], height[right_pointer])
            area = min_height*width

            if area > max_area:
                max_area = area
            if height[left_pointer] <= height[right_pointer]:
                left_pointer += 1
            else :
                right_pointer -= 1
        
        return max_area

        