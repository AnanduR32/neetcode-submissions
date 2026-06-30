from collections import deque as queue
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        maxFreq = 0
        maxCount = 0
        countMap:dict = dict()
        for right in range(len(s)):
            countMap[s[right]] = countMap.get(s[right], 0) + 1
            maxFreq = max(maxFreq, countMap[s[right]])

            while right - left + 1 - maxFreq > k:
                countMap[s[left]] -= 1
                left += 1
            
            maxCount = max(maxCount, right - left + 1)


        return maxCount
