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
        
        def threeSumForSorted(nums:List[int]):
            nums.sort()
            size = len(nums)
            output: List[List[int]] = list()
            curr, left, right = 0, 0, 0
            while curr < size:
                left = curr + 1
                right = size - 1
                sum3 = nums[curr] + nums[left] + nums[right]
                if sum3 == 0:
                    output.append([nums[curr], nums[left], nums[right]])
                    left += 1
                    while (nums[left] == nums[left - 1]):
                        left += 1
                    right -= 1
                    while (nums[right] == nums[right + 1]):
                        right -= 1
                elif sum3 > 0:
                    right -= 1
                    while (nums[right] == nums[right + 1]):
                        right -= 1
                else:
                    left += 1
                    while (nums[left] == nums[left - 1]):
                        left += 1
            return output

        if is_sorting_allowed:
            pass
        else:
            return threeSumRecursive(nums)

    
    