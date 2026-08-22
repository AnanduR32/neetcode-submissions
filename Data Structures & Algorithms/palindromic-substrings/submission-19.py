class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        count = 0
        
        def expand(i:int, j:int)-> None:
            nonlocal count
            while i >= 0 and j < size and s[i] == s[j]:
                i -= 1
                j += 1
                count += 1

        for i in range(0, size):
            expand(i, i)
            expand(i, i + 1)
    
        return count