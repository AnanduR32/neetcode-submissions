class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = {}
        for (idx,target) in enumerate(nums):
            results = self.twoSum(nums, target * -1, idx)
            for (first, second) in results:
                key = tuple(sorted([nums[idx],nums[first],nums[second]]))
                if key not in output:
                    output[key] = [target,nums[first],nums[second]]
        return list(output.values())
    
    def twoSum(self, nums:List[int], target:int, currIdx:int) -> List[(int, int)]:
        hDict = {}
        hOutout = {}
        for (idx, num) in enumerate(nums):
            if (idx == currIdx):
                continue
            complement = target - num
            if complement in hDict:
                key = tuple(sorted([hDict[complement], idx]))
                if key not in hOutout:
                    hOutout[key] = [hDict[complement], idx]
            hDict[num] = idx
        return list(hOutout.values())