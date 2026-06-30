class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data:dict = {}

        for string in strs:
            ordinal = [0] * 26
            for char in string:
                ordinal[ord(char) - 97] += 1
            key = tuple(ordinal)
            data.setdefault(key, []).append(string)
        
        return list(data.values())


    