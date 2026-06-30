class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False
        data: List = [0] * 26
        for idx in range(len(s)):
            data[ord(s[idx]) - 97] += 1
            data[ord(t[idx]) - 97] -= 1
        return all(x == 0 for x in data) 
        