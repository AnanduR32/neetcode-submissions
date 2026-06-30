class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data:dict = dict()
        for string in strs:
            key = tuple(sorted(x for x in string))
            data[key] = data.get(key, []) + [string]
        return list(data.values())