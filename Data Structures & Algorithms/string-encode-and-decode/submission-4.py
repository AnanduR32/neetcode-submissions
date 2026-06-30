class Solution:

    def encode(self, strs: List[str]) -> str:
        output: str = "" 
        for string in strs:
            length = len(string)
            output += f"{length}#{string}"
        return output

    def decode(self, s: str) -> List[str]:
        curr = 0
        length_str = len(s)
        output: List[str] = []
        while curr < length_str:
            digit_end = curr + s[curr:].find("#")
            n_char = s[curr:digit_end]
            n_digit = len(n_char)
            curr += n_digit + 1
            result: str = s[curr:int(n_char)+curr]
            curr += int(n_char)
            output.append(result)
        return output
