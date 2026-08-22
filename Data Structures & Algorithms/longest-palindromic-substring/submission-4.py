class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)

        output = s[0]
        def expand(i:int, j:int)-> None:
            nonlocal output
            while i >= 0 and j < size and s[i] == s[j]:
                if (j - i + 1) > len(output):
                    output = s[i:j+1]
                i -= 1
                j += 1

        for i in range(0, size):
            expand(i-1, i+1)
            expand(i, i + 1)
        return output

