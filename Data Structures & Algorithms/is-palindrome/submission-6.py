class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw = [x.lower() for x in s if x.isalpha() or x.isdigit()]
        return raw == raw[::-1]