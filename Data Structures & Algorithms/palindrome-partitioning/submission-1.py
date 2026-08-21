class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        size = len(s)
        def isPalindrome(start = 0, end = 1)->bool:
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def helper(start = 0, curr = []) -> None:
            nonlocal output
            if start == size:
                output.append(curr[:])
                return
            
            for end in range(start, size):
                if isPalindrome(start, end):
                    curr.append(s[start:end+1])
                    helper(end + 1)
                    curr.pop()


            
            
        helper()

        return output

