class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        space = [0]*26
        for n in range(len(s)):
            space[ord(s[n])-ord('a')] += 1
            space[ord(t[n])-ord('a')] -= 1
        return all(x == 0 for x in space)
        