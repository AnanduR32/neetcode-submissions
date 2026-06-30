class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictAnagrams = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char)-ord('a')] += 1
            key = tuple(count)
            if (key in dictAnagrams):
                dictAnagrams[key].append(string)
            else:
                dictAnagrams[key] = [string]
        return list(dictAnagrams.values())