class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        print(x)
        print(x[::-1])
        return x == x[::-1]