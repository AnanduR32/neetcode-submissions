import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = re.sub(r'[^A-Za-z0-9]+', "", s.lower())
        print(s_cleaned)
        s_cleaned_reversed = s_cleaned[::-1]
        if s_cleaned_reversed == s_cleaned:
            return True
        return False