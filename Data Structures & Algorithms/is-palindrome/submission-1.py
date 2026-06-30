import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = re.sub(r'[^A-Za-z0-9]+', "", s.lower())
        return s_cleaned == s_cleaned[::-1]