class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        space = [0 for x in range(26)]
        for char in s:
            space[ord(char)-97]+=1
        for char in t:
            space[ord(char)-97]-=1
        if any(x != 0 for x in space):
            return False
        return True
        