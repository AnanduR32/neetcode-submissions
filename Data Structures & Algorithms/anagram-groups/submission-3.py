class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_grams = {}
        for string in strs:
            output_list = [0 for x in range(26)]
            for char in string:
                output_list[ord(char.lower()) - 97]+=1
            output_str = ":".join(map(str, output_list))
            if output_str in str_grams:
                str_grams[output_str].append(string)
            else:
                str_grams[output_str] = [string]
        return [str_grams[x] for x in str_grams]