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
        digit: int = 0
        curr: int = 0
        left: int = 0
        right: int = 0
        size: int = len(s)
        while(curr < size):
            while(s[right+1].isdigit()):
                right += 1
            print(left,right)
            digit = int(s[left:right+1])
            sep_pos = right+1
            if (s[sep_pos] != '#'):
                print("errored")
            left = right + 1
            right = left + digit

            print(left,right)
            string = s[left+1:right+1]
            print(string)
            strs.append(string)
            curr = left = right = right + 1
            print(curr, left, right)
        return strs

