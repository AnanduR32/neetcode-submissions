class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictAnagrams = {}
        for string in strs:
            key = self.makeHashKey(string)
            if (key in dictAnagrams):
                dictAnagrams[key].append(string)
            else:
                dictAnagrams[key] = [string]
        return list(dictAnagrams.values())

    def makeHashKey(self, string: str) -> str:
        count = [0] * 26
        for char in string:
            count[ord(char)-ord('a')] += 1
        return "-".join(str(x) for x in count)