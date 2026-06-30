import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sr = s.replace(" ", "")
        srt = "".join([x.lower() for x in sr if x.isalpha() or x.isdigit()])
        return srt == srt[::-1]