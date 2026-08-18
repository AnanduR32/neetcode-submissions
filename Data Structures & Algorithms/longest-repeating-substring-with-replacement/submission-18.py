import heapq
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charsToCheck:set[str] = set()
        charCounts:dict = dict()
        q = []
        for char in s:
            charsToCheck.add(char)
            charCounts[char] = charCounts.get(char, 0) + 1

        for key,value in charCounts.items():
            heapq.heappush(q, (-value, key))
        
        # for char in charsToCheck:

        # charsToCheck = list(heapq.heappop(q))
        # while q and charsToCheck[0] == q[0][0]:
        #     charsToCheck.append(heapq.heappop(q)[1])
        
        maxLength = 0
        for char in charsToCheck:
            replaced = 0
            left = 0
            for right, ch in enumerate(s):
                if ch != char:
                    if replaced >= k:
                        while s[left] == char:
                            left += 1
                        left += 1
                        replaced -= 1
                    replaced += 1
                maxLength = max(maxLength, right - left + 1)
        
        return maxLength
            