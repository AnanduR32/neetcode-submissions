class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        size = len(digits)
        if not digits:
            return []
        mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        counts = {key:len(value) for key, value in mapping.items()}

        def helper(start = 0, curr = []):
            nonlocal output

            if len(curr) == size:
                output.append(''.join(curr))
                return
        
            for digit in mapping[digits[start]]:
                curr.append(digit)
                helper(start + 1, curr)
                curr.pop()
        
        helper()

        return output