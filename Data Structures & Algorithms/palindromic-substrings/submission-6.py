class Solution:
    def countSubstrings(self, s: str) -> int:
        
        left = 0
        right = 0
        count = 0
        validPalindromes:set[tuple] = set()
        for left in range(len(s)):
            for right in range(len(s)):
                flag = False
                if s[left] == s[right]:
                    curr = left
                    end = right
                    while curr + 1 < len(s) and curr + 1 < end - 1 and s[curr + 1] == s[end - 1]:
                        if (curr + 1,end) in validPalindromes:
                            count += 1
                            flag = True
                            break
                        validPalindromes.add((curr + 1,right))
                        curr += 1
                        end -= 1
                    if not flag and (curr == end - 1 or curr + 1 == end - 1 or curr == end):
                        count += 1
                        validPalindromes.add((left,right+1))
        return count                

                    

            

