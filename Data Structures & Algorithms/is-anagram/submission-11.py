class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        data:dict = {}
        for char in s:
            data[char] = data.get(char, 0) + 1
        for char in t:
            data[char] = data.get(char, 0) - 1
        return all(x == 0 for x in data.values()) 
        