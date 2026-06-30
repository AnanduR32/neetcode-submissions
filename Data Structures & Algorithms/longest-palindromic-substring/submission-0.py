class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        curr = 0
        maxLength = 0
        maxSubString: str = ''
        for idx, curr in enumerate(s):
            (margin_left, margin_right) = self.expand(s, idx)
            subString = s[margin_left: margin_right + 1]
            length = margin_right - margin_left + 1
            if length > maxLength:
                maxLength = length
                maxSubString = subString
            
            if idx + 1 < size and s[idx+1] == curr:
                (margin_left, margin_right) = self.expand(s, idx, 1)
                subString = s[margin_left: margin_right + 1]
                length = margin_right - margin_left + 1
                if length > maxLength:
                    maxLength = length
                    maxSubString = subString

        return maxSubString
    
    def expand(self, s:str, idx:int, offset:int = 0) -> tuple[int, int]:
        left = idx - 1
        right = idx + 1 + offset
        margin_left = idx
        margin_right = idx + offset
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            margin_left = left
            margin_right = right
            left -= 1
            right += 1
        
        return (margin_left, margin_right)
       
            
                    
            