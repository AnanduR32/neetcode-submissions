class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        count = 0
        for pos in range(len(s)):
            dp[pos][pos] = True
            count += 1
        for i in range(1, len(s)):
            for pos in range(len(s)):
                if pos + i >= len(s):
                    break
                if i == 1:
                    equals = s[pos] == s[pos+i]
                else:
                    equals = s[pos] == s[pos+i] and dp[pos + 1][pos + i - 1]
                dp[pos][pos+i] = equals
                count = count + 1 if equals else count
        return count
