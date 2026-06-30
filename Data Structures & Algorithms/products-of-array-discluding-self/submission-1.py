class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums[0]
        product = [1] * len(nums)

        for idx in range(1, len(nums)):
            product[idx] = product[idx - 1] * prefix
            prefix = nums[idx]

        for idx in range(len(nums) - 2, -1, -1):
            product[idx] = product[idx] * prefix
            prefix *= nums[idx]
        
        print(product)

        return product