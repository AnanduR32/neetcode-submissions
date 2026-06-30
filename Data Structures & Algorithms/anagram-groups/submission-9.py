class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data:dict = {}
        
        for string in strs:
            key = tuple(sorted(x for x in string))
            data.setdefault(key, []).append(string)
        
        return list(data.values())


    