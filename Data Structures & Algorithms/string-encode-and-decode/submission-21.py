class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + '#' + string
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        strs: List[str] = []
        string = ""
        deciphering = False
        curr = 0
        length = 0
        while curr < len(s):
            if s[curr] == '#' and not deciphering:
                if length == 0:
                    strs.append(string)
                else:
                    deciphering = True
                string = ""
            elif s[curr].isdigit() and not deciphering:
                length = length * 10 + int(s[curr])
            else:
                string += s[curr]
                length -= 1
                if length == 0:
                    deciphering = False
                    strs.append(string)
                    string = ""
            curr += 1
        return strs

