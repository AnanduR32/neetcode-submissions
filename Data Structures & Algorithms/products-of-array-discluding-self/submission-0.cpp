class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int size = nums.size();
        vector<int> output(size, 1);
        int prefix = 1;
        for (int i = 0; i < size; i++)
        {
            output[i] = prefix;
            prefix *= nums[i];
        }

        int postfix = 1;
        for (int i = size - 1; i >= 0; i--)
        {
            output[i] *= postfix;
            postfix *= nums[i];
        }

        return output;
    }
};
