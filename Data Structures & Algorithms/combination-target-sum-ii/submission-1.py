class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        output = []
        candidates.sort()
        def helper(start = 0, total = 0, curr = []):
            nonlocal output
            if total == target:
                output.append(curr[:])
            if total >= target:
                return

            for idx in range(start, size):
                val = candidates[idx]
                
                if total + val > target:
                    break

                if idx > start and candidates[idx] == candidates[idx - 1]:
                    continue
                
                curr.append(val)
                helper(idx + 1, total + val, curr)
                curr.pop()
        
        helper()

        return output