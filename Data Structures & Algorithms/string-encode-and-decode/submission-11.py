class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            prefix = str(len(string)) + '#' + string
            encoded += prefix
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        strs: list[str] = []
        string: str = ""
        reading: bool = False
        isDigitParsed: bool = False
        digit: int = 0
        for char in s:
            if (char.isdigit() and not isDigitParsed):
                digit = digit * 10 + int(char)
            elif (char == '#' and not isDigitParsed):
                if (digit == 0):
                    strs.append(string)
                    continue
                isDigitParsed = True

            elif (isDigitParsed and digit > 0):
                string += char
                digit-=1
                if (digit == 0):
                    isDigitParsed = False
                    strs.append(string)
                    string = ""
        return strs

