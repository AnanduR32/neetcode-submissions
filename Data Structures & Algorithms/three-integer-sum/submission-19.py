class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        is_sorting_allowed = False

        def threeSumRecursive(nums):
            seen = set()
            output:List[List[int]] = list()
            def doTwoSum(idx:int, arr:List)->List[List[int]]:
                target = nums[idx]
                offset = idx + 1
                complements = dict()
                output:List[List[int]] = list()
                for itr,num in enumerate(arr):
                    complement = -(target + num)
                    if complement in complements:
                        output.append([offset+complements[complement],offset+itr])
                    complements[num] = itr
                return output

            for idx, num in enumerate(nums):
                positions_list = doTwoSum(idx, nums[idx + 1:])
                for positions in positions_list:
                    out = [nums[idx]]+[nums[x] for x in positions]
                    key = tuple(x for x in sorted(out))
                    if key in seen:
                        continue
                    seen.add(key)
                    output.append(out)
            return output
        
        def threeSumForSorted():
            pass

        if is_sorting_allowed:
            pass
        else:
            return threeSumRecursive(nums)

    
    