class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen:set[str] = set()
        maxLength = 0
        left = 0
        for curr, char in enumerate(s):
            if char in seen:
                while s[left] != char:
                    seen.remove(s[left])
                    left += 1
                left += 1
            seen.add(char)
            maxLength = max(maxLength, curr - left + 1)
        
        return maxLength
