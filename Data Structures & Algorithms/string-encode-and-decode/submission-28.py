class Solution:

    def encode(self, strs: List[str]) -> str:
        output:str = ""
        for string in strs:
            output += str(len(string)) + "#" + string
        return output

    def decode(self, s: str) -> List[str]:
        i = 0
        size = len(s)
        output = []
        while i < size:
            j = i
            while s[j].isdigit():
                j += 1
            digit = int(s[i:j])
            i = j + 1 + digit
            string = s[j + 1:i]

            output.append(string)
        return output
                