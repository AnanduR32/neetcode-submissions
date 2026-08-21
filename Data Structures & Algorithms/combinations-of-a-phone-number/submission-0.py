class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        size = len(digits)

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
                if any(x != '' for x in curr):
                    output.append(''.join(curr))
            
            for idx in range(start, size):
                for digit in mapping[digits[idx]]:
                    curr.append(digit)
                    helper(idx + 1, curr)
                    curr.pop()
        
        helper()

        return output