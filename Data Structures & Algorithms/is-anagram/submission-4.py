class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        space = { }
        for char in s:
            if char in space:
                space[char] += 1
            else:
                space[char] = 1
        for char in t:
            if char in space:
                space[char] -= 1
            else:
                space[char] = -1
        print (space)
        if any(y != 0 for (x,y) in space.items()):
            return False
        return True
        