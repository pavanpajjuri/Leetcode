class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        score = 0
        maj_element = None

        for element in nums:
            if score == 0:
                maj_element = element
                score = score + 1
            elif element == maj_element:
                score = score + 1
            else:
                score = score - 1
        
        # print(score)
        return maj_element
        