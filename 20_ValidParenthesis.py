class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        opening_braces = '({['
        closing_braces = ')}]'
        matching_brace = {
            '(':')',
            '{':'}',
            '[':']'
        }
        for char in s:
            if char in opening_braces:
                arr.append(char)
            elif char in closing_braces:
                if(len(arr)==0):
                    return False
                prev_brace = arr.pop()
                if(char != matching_brace[prev_brace]):
                    return False
        return True        
                
            




