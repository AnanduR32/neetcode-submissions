class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        memo = [[True if x == y and x > 0 else False for y in range(size + 1)] for x in range(size + 1)]
        count = size
        for i in range(size, 0, -1):
            for j in range(i + 1, size + 1):
                if s[i-1] == s[j-1] and (j-i <= 2 or memo[i+1][j-1]):
                    memo[i][j] = True
                    count += 1
    
        return count